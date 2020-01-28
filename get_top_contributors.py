import most_common_words
def get(words_list, number, unique_words_length) : 
    percent_count = len(words_list) *15/100
    top_list = []
    words_frequency = most_common_words.get_top(words_list,unique_words_length)
    i = 0
    while(percent_count>0) : 
        percent_count -= words_frequency[i][1]
        top_list.append(words_frequency[i][0])
        i+=1
    return top_list