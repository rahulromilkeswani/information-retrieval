import nltk
sw = open("stopwords.txt","r") 
stopwords = nltk.word_tokenize(sw.read())
def remove(words_list) : 
    filtered_words = []
    filtered_words = [word for word in words_list if word not in stopwords] 
    return filtered_words

def get_difference(words_list) : 
    return list(set(words_list) & set(stopwords))
