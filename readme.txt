1) The modules' documentation is provided in documentation.txt

2) Requirements : 
        i)  Place all the files in a working directory. 

        ii) Install Python version 3.x

        iii) Install nltk library 
            --- use ' pip install nltk ' to download and install it on the machine. 

        iv) Uncomment ' nltk.download('punkt') ' in tokenizer.py while running for the first time. 
             Comment it back after first run. 

        v) Execute the main.py


3) Answers : 

    2)
        a) The total number of words in the corpus are : 476263

        b) The number of unique words in the corpus are : 19885

        c) The top 20 words in the corpus with most occurences are :
            ['the', 'of', 'and', 'a', 'to', 'in', 'for', 'is', 'we', 'that', 'this', 'are', 'on', 'an', 'with',
             'as', 'by', 'data', 'be', 'information']

        d) The top 20 words which are stop words are :
            ['that', 'an', 'we', 'be', 'a', 'and', 'in', 'are', 'of', 'on', 'to', 'is', 'this', 'by', 'the',
             'as', 'with', 'for']

        e) The top 15 percent contributor words among all words are : 4

    3)

    `   a) The number of words in the corpus after removing stopwords and stemming are : 265776

        b) The number of unique words in the corpus after removing stopwords and stemming are : 13556

        c) The top 20 words in the corpus after removing stopwords and stemming with most occurences are :
            ['system', 'data', 'agent', 'inform', 'model', 'paper', 'queri', 'user',
             'learn', 'algorithm', '1', 'approach', 'problem', 'applic', 'present', 'base', 'web', 'databas',
              'comput', 'method', 'web', 'databas', 'comput', 'method']

        d) The top 20 words which are stop words after removing stopwords and stemming are :
            []

        e) The top 15 percent contributor words among all words after removing stopwords and stemming are : 22