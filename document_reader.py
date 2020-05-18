import os,glob
import string
import json

def read_documents(name):
    documents = []
    path = name+"/"
    for filename in sorted(os.listdir(path)):
        with open(path+filename, "r") as f:
                documents.append(f.read())
    return documents

def remove_punctuations(documents) : 
    trimmed_documents = []
    for document in documents:
                document = document.replace('\r', '').replace('\n', ' ').lower()  
                trimmed_document = out = document.translate(str.maketrans("","", string.punctuation))
                trimmed_documents.append(trimmed_document)
    return trimmed_documents

def read_query(name):
    lines = []
    with open(name) as f:
        lines = [line.rstrip() for line in f]
    return lines

def read_relevance(name):
    lines = []
    with open(name) as f:
        lines = [line.split() for line in f]
    return lines


def get_required_documents(abstract_folder_name,gold_folder_name) : 
    gold_files = []
    abstract_files = []
    gold_path = gold_folder_name+"/"
    abstract_path = abstract_folder_name+"/"

    for filename in sorted(os.listdir(gold_path)):
        gold_files.append(filename)
    for filename in sorted(os.listdir(abstract_path)):
        abstract_files.append(filename)

    return list(set(gold_files) & set(abstract_files))


def read_abstracts(required_abstracts,abstract_folder_name) : 
    documents = []
    path = abstract_folder_name+"/"
    for filename in sorted(os.listdir(path)):
        if filename in required_abstracts : 
            with open(path+filename, "r") as f:
                    documents.append(f.read())
    return documents


def read_json_files(folder_name) : 
    json_files = []
    for filename in sorted(os.listdir(folder_name)):
         with open(folder_name+"/"+filename, "r") as f:
             try:
                json_files.append(json.load(f))
             except:
                 continue
    return json_files


