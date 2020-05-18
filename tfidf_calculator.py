import math
def calculate_document_tfidf(documents,dictionary) : 
    document_weight_dict = {}
    document_weight_squared = {}
    i=1
    for document in documents : 
        word_weight = {}
        squared_word_weight=0
        for word in set(document) : 
            tf = (dictionary[word].get(i))/len(document)
            idf = math.log2(len(documents)/len(dictionary[word]))
            word_weight[word] = tf*idf
            squared_word_weight = squared_word_weight + (word_weight[word]**2)
        document_weight_dict[i]=(word_weight)
        document_weight_squared[i]=squared_word_weight
        i=i+1
    return document_weight_dict,document_weight_squared


def calculate_query_tfidf(queries,documents,dictionary) : 
    query_weight = {}
    i=1
    for query in queries : 
        query_token_weights = {}
        for word in query : 
            if(word in dictionary) : 
                tf = query.count(word)/len(query)
                idf = math.log2(len(documents)/len(dictionary[word]))
                query_token_weights[word] = tf*idf
        query_weight[i] = query_token_weights
        i=i+1
    return query_weight 