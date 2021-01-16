def general_text_processing(txtfile):   
    """Takes in a txtfile and does general preprocessing to text data 
    flatten/ sperate on comma/ tokenize/ lower words/ remove basic stop words 
    Requires nltk package"""  
    import nltk
    #open file 
    file = open(txtfile) 
    yourResult = [line.split(',') for line in file.readlines()] 
    flat_text = [item for sublist in yourResult for item in sublist] 
    #open and flatten file
    file_raw = open_and_flatten(txtfile) 
    #seperate file on , -  
    seperator = ","
    joined_file = seperator.join(file_raw)  
    #tokenize string
    pattern = "([a-zA-Z]+(?:'[a-z]+)?)"
    joined_file_tokens = nltk.regexp_tokenize(joined_file, pattern)  
    #set all words to lower case
    joined_file_words_lowered = [word.lower() for word in joined_file_tokens] 
    #remove general stopwords 
    stopwords_list = stopwords.words('english')
    stopwords_list += list(string.punctuation)
    stopwords_list += ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Student','Name','School',
                       'The', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                       'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'st']
    joined_file_words_stopped = [word for word in joined_file_words_lowered if word not in stopwords_list] 
    return joined_file_words_stopped  

def word_cloud(word_list): 
    """Input: A list of words 
    Output: a word cloud""" 
    unique_string=(" ").join(word_list)
    wordcloud = WordCloud(width = 1000, height = 500, max_font_size=50, max_words=100,
                      background_color="white", colormap="gray_r").generate(unique_string)
    plt.figure(figsize=(12,6))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig("your_file_name"+".png", bbox_inches='tight')
    plt.show()
    plt.close() 