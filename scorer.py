
import nltk
import numpy as np
import pandas as pd
from nltk.stem import PorterStemmer
stemmer=PorterStemmer()


def calculate_word_score(graphs) : 
     alpha = 0.85
     document_scores = []
     for graph in graphs :
              number_of_nodes = len(list(graph.nodes())) 
              scores = {}
              for node in list(graph.nodes()):
                  scores[node] = 1/number_of_nodes
              for i in range(0,10) : 
                for node in list(graph.nodes()): 
                        weights_sum = 0
                        for adjacent_node in list(graph.neighbors(node)): 
                            node_weight = 0  
                            adjacent_node_weight = 0
                            for next_adjacent_node in list(graph.neighbors(adjacent_node)): 
                                if(graph.has_edge(adjacent_node,next_adjacent_node)):
                                    adjacent_node_weight += graph.get_edge_data(adjacent_node,next_adjacent_node)['weight']
                            if(adjacent_node_weight>0):
                                node_weight = graph.get_edge_data(node,adjacent_node)['weight']
                                weights_sum += (node_weight/adjacent_node_weight)*scores[adjacent_node]
                        scores[node] = (alpha*weights_sum) + ((1-alpha)*(1/number_of_nodes))
              document_scores.append(scores)
     return document_scores





def calculate_ngram_score(documents, scores, document_nodes):
    documents_sorted_phrase_score = []
    for i,document in enumerate(documents) : 
        score = scores[i]
        phrase_score = {}
        bigram = list(nltk.ngrams(document.split(), 2))
        trigrams= list(nltk.ngrams(document.split(), 3))
        document_node = document_nodes[i]
        for word in document.split():
            if (word.endswith("NN") or word.endswith("NNS") or word.endswith("NNP") or word.endswith("NNPS")) : 
                word = stemmer.stem(word.split("_")[0])
                if(word in document_node) : 
                    phrase_score[word] = 0
                    if score.get(word) is not None : 
                        phrase_score[word]+=score.get(word)
        for word1, word2 in bigram:
            if (word2.endswith("NN") or word2.endswith("NNS") or word2.endswith("NNP") or word2.endswith("NNPS")) : 
                word1 = stemmer.stem(word1.split("_")[0])
                word2 = stemmer.stem(word2.split("_")[0])
                if(word1 in document_node and word2 in document_node) : 
                    phrase_score[word1 + " " + word2] = 0
                    if score.get(word1) is not None : 
                        phrase_score[word1 + " " + word2]+=score.get(word1)
                    if score.get(word2) is not None : 
                        phrase_score[word1 + " " + word2]+=score.get(word2)
        for word1, word2, word3 in trigrams:
            if (word3.endswith("NN") or word3.endswith("NNS") or word3.endswith("NNP") or word3.endswith("NNPS")) : 
                word1 = stemmer.stem(word1.split("_")[0])
                word2 = stemmer.stem(word2.split("_")[0])
                word3 = stemmer.stem(word3.split("_")[0])
                if(word1 in document_node and word2 in document_node and word3 in document_node) : 
                    phrase_score[word1 + " " + word2 + " " + word3] = 0
                    if score.get(word1) is not None : 
                        phrase_score[word1 + " " + word2 + " " + word3]+=score.get(word1)
                    if score.get(word2) is not None : 
                        phrase_score[word1 + " " + word2 + " " + word3]+=score.get(word2)
                    if score.get(word3) is not None : 
                        phrase_score[word1 + " " + word2 + " " + word3]+=score.get(word3)

        sorted_phrase_score = sorted(phrase_score.items(), key=lambda x: x[1], reverse=True)
        documents_sorted_phrase_score.append(sorted_phrase_score)
    return documents_sorted_phrase_score


def calculate_mrr_score(documents_sorted_phrase_score, gold_documents) : 
    mmr_scores = []
    for i,document_sorted_phrase_score in enumerate(documents_sorted_phrase_score) : 
        gold_document = gold_documents[i]
        top_phrases = []
        top_phrases_scores = []
        limit = 10
        if(len(document_sorted_phrase_score)<limit) : 
            limit = len(document_sorted_phrase_score)
        for count in range(0,limit) : 
            if document_sorted_phrase_score[count] is not None : 
                top_phrases.append(document_sorted_phrase_score[count][0])
                top_phrases_scores.append(document_sorted_phrase_score[count][1])
        doc_mmr_score = []
        for j in range (0,limit) : 
            mrr_score = 0
            for k in range (0,j+1):
                if top_phrases[k] in gold_document : 
                    mrr_score =  (1/(k+1))
                    break
            doc_mmr_score.append(mrr_score)
        mmr_scores.append(doc_mmr_score)
    mrr_score_df = pd.DataFrame(mmr_scores)
    mrr_averages = mrr_score_df.mean()
    return mrr_averages

def calculate_page_score(graph) : 
    e = 0.15
    number_of_nodes = len(list(graph.nodes())) 
    scores = {}
    for node in list(graph.nodes()):
        scores[node] = 1/number_of_nodes
    for i in range(0,50) : 
        old_scores = scores
        for node in list(graph.nodes()) : 
            weighted_sum = 0
            for neighbor in list(graph.predecessors(node)): 
                if not len(list(graph.neighbors(neighbor))) == 0 : 
                    weighted_sum += old_scores[neighbor] / len(list(graph.neighbors(neighbor)))
            scores[node] = ((1-e)*weighted_sum) + (e/number_of_nodes)
    return scores

def calculate_combined_scores(cos_sim_map,page_scores):         
    combined_page_scores = {}
    for j in range(0,len(cos_sim_map)) : 
        for i,page_score in enumerate(page_scores) : 
            page_score_value = page_scores[page_score]
            cos_sim_score = cos_sim_map[j+1].get(i+1)
            if(cos_sim_score is not None) : 
             #combined_page_scores[page_score] = (2*page_score_value*cos_sim_score)/(cos_sim_score+page_score_value)
                combined_page_scores[page_score] = (0.1*page_score_value)+(0.9*cos_sim_score)

    sorted_page_score = sorted(combined_page_scores.items(), key=lambda x: x[1], reverse=True)
    return sorted_page_score
