def build_dictionary(documents): 
    inverted_dictionary = {}
    i=1
    for document in documents :
        for word in document : 
            document_dictionary = {}
            if word not in inverted_dictionary:
                document_dictionary[i]=1
                inverted_dictionary[word]=document_dictionary
            else:
                child_dictionary=inverted_dictionary.get(word)
                if i not in child_dictionary.keys():
                    child_dictionary[i]=1
                else:
                    child_dictionary[i]+=1
        i=i+1
    return inverted_dictionary
    
            

