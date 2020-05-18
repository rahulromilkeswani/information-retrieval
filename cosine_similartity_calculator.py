import math
def cosine_similarity(query_weights, documents, document_weights, squared_document_weights):
    cosine_sim = {}
    for i, query in enumerate(query_weights) : 
        query_doc_sim = {}
        for j, document in enumerate(documents) :
            document_map = documents[document]
            numerator = 0
            if(set(query_weights[query].keys()) & set(document_map.keys())): 
                for word in (set(query_weights[query].keys()) & set(document_map.keys())) : 
                    numerator+=(query_weights[query].get(word))*(document_weights[j+1].get(word))
                denominator = math.sqrt(squared_document_weights[j+1])
                query_doc_sim[j+1] = (numerator/denominator)
        cosine_sim[i+1] = query_doc_sim
    return cosine_sim


def sort_cosine_similarity(cosine_similarities) : 
    sorted_cos_sim = {}
    for similarity in cosine_similarities : 
        sorted_values = sorted(cosine_similarities[similarity].items(), key=lambda kv: kv[1],reverse = True)
        sorted_cos_sim[similarity] = sorted_values
    return sorted_cos_sim
        
def calculate_precision_recall(sorted_cos_sim, top_n , query_number, relevances) : 
    retrieved = []
    for i in range(0,top_n) : 
        retrieved.append(sorted_cos_sim[query_number][i][0])
    relevant = []
    for relevance in relevances : 
        if(int (relevance[0])==query_number) : 
            relevant.append(int(relevance[1]))
    common = len(set(retrieved) & set(relevant))
    precision = common / len(retrieved)
    recall = common / len(relevant)
    return precision,recall