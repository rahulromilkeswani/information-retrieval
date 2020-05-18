import nltk
sw = open("stopwords.txt","r") 
stopwords = nltk.word_tokenize(sw.read())
def remove(words_list) : 
    filtered_words = []
    for line in words_list:
        inner=[]
        for word in line:
            if word not in stopwords:
                inner.append(word)
        filtered_words.append(inner)
    return filtered_words

def get_difference(words_list) : 
    return list(set(words_list) & set(stopwords))


def remove_from_document(documents) : 
    filtered_documents = []
    for document in documents : 
        filtered_document = []
        for word in document : 
             if word not in stopwords:
                filtered_document.append(word)
        filtered_documents.append(filtered_document)
    return filtered_documents
