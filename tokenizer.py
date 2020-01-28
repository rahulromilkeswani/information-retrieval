import nltk 
#nltk.download('punkt')
def get_all_tokens(documents):
    tokens = []
    for document in documents : 
        tokens.append(nltk.word_tokenize(document))
    all_tokens = [y for x in tokens for y in x]
    return all_tokens
def get_unique_tokens(words_list) : 
    unique_words = []
    unique_words = list(set(words_list))
    return unique_words

