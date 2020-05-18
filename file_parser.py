from bs4 import BeautifulSoup

def get_elements(documents) : 
    required_documents = []
    for document in documents : 
        soup = BeautifulSoup(document,features = "html.parser")
        required_text=soup.find('title').getText() + soup.find('text').getText()
        required_documents.append(required_text)
    return required_documents


def get_links(documents) : 
    title_link = {}
    document_links = []
    for document in documents : 
        document_links.append(document.get("url"))
        title_link[document.get("url")] = document.get("title")
    return document_links, title_link




def get_document_text(documents) : 
    documents_text = []
    for document in documents : 
        document_text = document.get("title")+". "
        for line in document.get("text") : 
            document_text += line
        documents_text.append(document_text)
    return documents_text

def get_out_links(documents) : 
    out_links = []
    for document in documents : 
        out_links.append(document.get("out_links"))
    return out_links