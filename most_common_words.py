from nltk import FreqDist
def get_top(words_list, quantity):
    fdist = FreqDist(words_list)
    top_words = fdist.most_common(quantity)
    return top_words

def get_top_list(words_list,quantity):
    fdist = FreqDist(words_list)
    top_words = fdist.most_common(quantity)
    top_words_list = []
    for i in range(quantity) : 
            top_words_list.append(top_words[i][0])
    return top_words_list

