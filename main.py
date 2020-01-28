import file_extractor 
import document_reader
import tokenizer
import most_common_words
import get_top_contributors
import stopwords_remover
import stemmer


#file_extractor.extract_files() 
documents = document_reader.read_documents() 
all_tokens = tokenizer.get_all_tokens(documents) 
print("The total number of words in the corpus are : " +str(len(all_tokens)))

unique_tokens = tokenizer.get_unique_tokens(all_tokens)
print("\nThe number of unique words in the corpus are : " +str(len(unique_tokens)))

top_twenty_words = most_common_words.get_top_list(all_tokens, 20)
print("\nThe top 20 words in the corpus with most occurences are : \n" + str(top_twenty_words))

top_stop_words = stopwords_remover.get_difference(top_twenty_words)
print("\nThe top 20 words which are stop words are : \n" + str(top_stop_words))


top_fifteen_percent = get_top_contributors.get(all_tokens,15,len(unique_tokens))
print("\nThe top 15 percent contributor words among all words are : " +str(len(top_fifteen_percent)))

filtered_tokens = stopwords_remover.remove(all_tokens)
filtered_tokens = stemmer.get_stemmed_words(filtered_tokens)
print("\nThe number of words in the corpus after removing stopwords and stemming are : " + str(len(filtered_tokens)))

fitlered_unique_tokens = tokenizer.get_unique_tokens(filtered_tokens)
print("\nThe number of unique words in the corpus after removing stopwords and stemming are  : " +str(len(fitlered_unique_tokens)))

filtered_top_twenty_words = most_common_words.get_top_list(filtered_tokens, 20)
print("\nThe top 20 words in the corpus after removing stopwords and stemming are with most occurences are : \n" + str(filtered_top_twenty_words))

top_filtered_stop_words = stopwords_remover.get_difference(filtered_top_twenty_words)
print("\nThe top 20 words which are stop words after removing stopwords and stemming are  : \n" + str(top_filtered_stop_words))


filtered_top_fifteen_percent = get_top_contributors.get(filtered_tokens,15,len(fitlered_unique_tokens))
print("\nThe top 15 percent contributor words among all words after removing stopwords and stemming are  : " +str(len(filtered_top_fifteen_percent)))