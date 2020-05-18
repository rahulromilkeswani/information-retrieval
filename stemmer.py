from nltk.stem import PorterStemmer
stemmer=PorterStemmer()

def get_stemmed_words(words_list): 
    stemmed_words=[]
    stemmed_words=[stemmer.stem(word) for word in words_list]
    return stemmed_words

def remove_small_words(words_list) : 
    tokens=[]
    for line in words_list:
        words=[]
        for word in line:
            if(len(word)>=3):
                words.append(word)
        tokens.append(words)
    tokenized=[[word for word in arr if word.isalpha()] for arr in tokens]
    return tokenized


def stem_documents(documents):
    stemmed_documents=[]
    for document in documents : 
        stemmed_documents.append([stemmer.stem(word) for word in document])
    return stemmed_documents

def get_required_text(documents): 
    temp_documents = []
    for document in documents : 
        temp_document = []
        for word in document.split() : 
             if word.endswith(("_NN","_JJ")) :
                 word = word[:-3]     
                 if len(word) > 1 : 
                        temp_document.append(word.lower())      
             if word.endswith(("_NNS","_NNP")) :
                 word = word[:-4]  
                 if len(word) > 1 : 
                        temp_document.append(word.lower())      
             if word.endswith(("_NNPS")) :
                 word = word[:-5]  
                 if len(word) > 1 : 
                        temp_document.append(word.lower())                         
        temp_documents.append(temp_document)
    return temp_documents


def get_text(documents): 
    temp_documents = []
    for document in documents : 
        temp_document = []
        for word in document.split() : 
            word = word.split("_")[0]
            if(len(word)>1) : 
             temp_document.append(word.lower())
                
        temp_documents.append(temp_document)
    return temp_documents

# def parse_tags(documents):
#     tags = []
#     for document in documents :
#         for word in document.split():
#             split_tags = word.split("_");
#             if len(split_tags) > 1:
#                 tags.append(split_tags[1])
#     return set(tags)


def stem_phrases(documents):
    stemmed_documents=[]
    for document in documents :
        stemmed_lines = [] 
        for line in document.split("\n") : 
            current_line = []
            current_line.append([stemmer.stem(word) for word in line.split()])
            stemmed_lines.append(current_line)
        stemmed_documents.append(stemmed_lines)
    stemmed_phrases = []
    for document in stemmed_documents : 
        document_phrases = []
        for i in range(len(document)-1): 
            phrase = ""
            for phrases in document[i] : 
                for word in phrases : 
                    phrase+=word + " " 
            document_phrases.append(phrase.strip())
        stemmed_phrases.append(document_phrases)
    return stemmed_phrases