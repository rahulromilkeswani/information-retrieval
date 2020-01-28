from nltk.stem import PorterStemmer
def get_stemmed_words(words_list): 
    stemmed_words=[]
    stemmer=PorterStemmer()
    stemmed_words=[stemmer.stem(word) for word in words_list]
    return stemmed_words