#load the expanded ngs standards pdf into a txt file
def pdf_to_text(filepath, filename):  
    """takes in a local PDF file path and saves it as a local txt.file"""
    import pdftotext
    with open(filepath, "rb") as f:
        pdf = pdftotext.PDF(f)
 
    # Save all text to a txt file.
    with open(filename, 'w') as f:
        f.write("\n\n".join(pdf))  


#openfile and flatten into single list item
def open_and_flatten(filename): 
    """takes in a local txt file path and returns a flattened file"""
    file = open(filename) 
    yourResult = [line.split(',') for line in file.readlines()] 
    flat_text = [item for sublist in yourResult for item in sublist] 
    return flat_text 


def write_multiple_pdfs_to_text(path_list, filename):  
    """takes in multiple local PDF file path and saves it as a local txt.file""" 
    import PyPDF2
    for file in path_list: 
        with open(file, mode='rb') as f:
            reader = PyPDF2.PdfFileReader(f) 
            number_of_pages = reader.getNumPages()  
            for page in range(number_of_pages):   
                page = reader.getPage(page) 
                file = open(filename, 'a')
                sys.stdout = file
                print(page.extractText()) 
                file.close()   
                
                
def general_processing(txtfile):   
    """Takes in a txtfile and does general preprocessing to text data 
    flatten/ sperate on comma/ tokenize/ lower words/ remove basic stop words"""
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
                       'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'questions', 'science', 'st']
    joined_file_words_stopped = [word for word in joined_file_words_lowered if word not in stopwords_list] 
    return joined_file_words_stopped