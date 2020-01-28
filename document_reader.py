import os,glob
import string
def read_documents():
    documents = []
    path = "citeseer/"
    for filename in os.listdir(path):
        with open(path+filename, "r") as f:
            for line in f:
                line = line.replace('\r', '').replace('\n', '').lower()  
                trimmed_line = out = line.translate(str.maketrans("","", string.punctuation))
                documents.append(trimmed_line)
    return documents