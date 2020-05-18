import file_extractor
import document_reader
import file_parser
import tokenizer
import stemmer
import stopwords_remover
import most_common_words
import word_document_frequency
import tfidf_calculator
import cosine_similartity_calculator
import graphy
import scorer
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import networkx as nx
import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet




class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'UIC search Engine'
        self.parsed_files_path = "uic_scraper/files"

        self.json_files = document_reader.read_json_files(self.parsed_files_path)
        print("Read json files...")

        self.document_links, self.title_link = file_parser.get_links(self.json_files)
        print("Got nodes to create graph...")
        self.nodes = []
        self.nodes.append(self.document_links)
        self.document_graph = graphy.created_directed_graph(self.nodes)
        print("Created graph...")

        self.out_links = file_parser.get_out_links(self.json_files)
        print("Got out links for nodes...")

        self.edged_graph = graphy.add_link_edges(self.document_graph,self.document_links,self.out_links)
        print("Added edges to graph...")

        self.page_scores = scorer.calculate_page_score(self.edged_graph)
        print("Calculated scores...")


        self.parsed_documents = file_parser.get_document_text(self.json_files)
        print("Read documents...")

        self.trimmed_documents = document_reader.remove_punctuations(self.parsed_documents)
        print("Removed punctuations from documents...")

        self.tokenized_documents = tokenizer.tokenize_documents(self.trimmed_documents)
        print("Converted documents sentences into tokens...")

        self.stemmed_documents = stemmer.stem_documents(self.tokenized_documents)
        print("Stemmed all tokens in the documents...")

        self.filtered_documents = stopwords_remover.remove(self.stemmed_documents)
        self.large_documents = stemmer.remove_small_words(self.filtered_documents)
        print("Removed small tokens from the documents...")


        self.dictionary = word_document_frequency.build_dictionary(self.large_documents)
        print("Built bag of words dictionary...")

        self.tf_idf_dictionary,self.document_weight_squared = tfidf_calculator.calculate_document_tfidf(self.large_documents,self.dictionary)
        print("Built tf-idf for documents...")

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(10,10,1200,700)
        self.logo = QLabel(self)
        pixmap = QPixmap('uiclogo.png')
        self.logo.setPixmap(pixmap)
        self.setMenuWidget(self.logo)
        self.resize(pixmap.width(), pixmap.height())
        self.search_textbox = QLineEdit(self)
        self.search_textbox.move(720, 120)
        self.search_textbox.resize(380, 30)
        self.search_button = QPushButton('Search UIC', self)
        self.search_button.move(780, 160)
        self.search_button.clicked.connect(self.fetch_results)
        self.show_more_button = QPushButton('Show more..', self)
        self.show_more_button.move(900, 160)
        self.show_more_button.resize(160,30)
        self.show_more_button.clicked.connect(self.get_more_links)
        self.fetched_results = QTextBrowser(self)
        self.fetched_results.move(520, 260)
        self.fetched_results.resize(800, 770)    
        self.showFullScreen()


    @pyqtSlot()
    def fetch_results(self):
        self.page_size = 10
        query = self.search_textbox.text()
        results = self.get_results(query)
        html_content = ''
        self.url_list = []
        for url, score in results:
            title = self.title_link[url]
            html_content += title+'<br><a href="' + url + '">' + url + '</a><br><br>'
            self.url_list.append(title+'<br><a href="' + url + '">' + url + '</a><br><br>')

        urls = ''.join(self.url_list[:self.page_size])
        self.fetched_results.setText(urls)
        self.fetched_results.setOpenExternalLinks(True)


    @pyqtSlot()
    def get_more_links(self):
        self.page_size = self.page_size + 10
        self.fetched_results.setText(''.join(self.url_list[:self.page_size]))

    def get_results(self,query) : 
        queries= []
        queries.append(query)
        trimmed_queries = document_reader.remove_punctuations(queries)
        print("Removed punctuations from queries...")
        tokenized_queries = tokenizer.tokenize_documents(trimmed_queries)
        print("Converted query sentences into tokens...")
        expanded_queries = []
        for query_term in tokenized_queries[0] : 
            synsets = wordnet.synsets(query_term)
            if(len(synsets)!=0)  : 
                for lemma in synsets[0].lemmas() : 
                    for temp_lema in lemma.name().split("_") : 
                        temp_list= []
                        temp_list.append(temp_lema)
                        expanded_queries.append(temp_list)
            else : 
                expanded_queries = tokenized_queries 
        stemmed_queries = stemmer.stem_documents(tokenized_queries)
        print("Stemmed all tokens in the queries...")
        filtered_queries = stopwords_remover.remove(stemmed_queries)
        large_queries = stemmer.remove_small_words(filtered_queries)
        print("Removed small tokens from the queries...\n")
        tf_idf_query_dictionary = tfidf_calculator.calculate_query_tfidf(large_queries,self.large_documents,self.dictionary) 
        print("Built tf-idf for queries...\n")
        cos_sim_map = cosine_similartity_calculator.cosine_similarity(tf_idf_query_dictionary,self.tf_idf_dictionary,self.tf_idf_dictionary,self.document_weight_squared)
        print("Calculated cosine similarities for documents and queries...\n")
        combined_scores = scorer.calculate_combined_scores(cos_sim_map,self.page_scores)
        print("Calculated combined scores for pages...\n")
        return combined_scores



app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec_())