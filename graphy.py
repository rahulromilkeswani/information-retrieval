import networkx as nx
import matplotlib.pyplot as plt
import nltk


def create_graph(node_documents) :  
    document_graphs = [] 
    for document in node_documents : 
        graph = nx.Graph() 
        for word in document : 
            graph.add_node(word)
        document_graphs.append(graph)  
    return document_graphs

def add_edges(document_graphs,original_documents,window_size) :
    edged_document_graphs = [] 
    for i in range(0,len(document_graphs)) : 
        document_graph = document_graphs[i]
        original_document = original_documents[i]
        ngrams = list(nltk.ngrams(original_document,int(window_size)))
        for ngram in ngrams : 
            current_node = ngram[0]
            possible_neighbors = ngram[1:]  
            if(document_graph.has_node(current_node)) : 
                for word in possible_neighbors : 
                    if(document_graph.has_node(word)) :
                         if document_graph.has_edge(current_node, word) : 
                                document_graph[current_node][word]['weight'] += 1
                                #document_graph[word][current_node]['weight']+=1
                         else :  
                                document_graph.add_edge(current_node,word,weight=1)
        edged_document_graphs.append(document_graph)
    return edged_document_graphs

def created_directed_graph(node_documents)  : 
    graph = nx.DiGraph()
    for word in node_documents[0] : 
        graph.add_node(word)
    return graph

def add_link_edges(graph,node_links,out_links) :
    egded_graph = graph  
    for i in range (0,len(node_links))  :
        node = node_links[i]
        node_out_links = out_links[i] 
        for out_link in node_out_links : 
            if(egded_graph.has_node(out_link))  :
                if not egded_graph.has_edge(node, out_link) : 
                   egded_graph.add_edge(node,out_link)
    return egded_graph                     

