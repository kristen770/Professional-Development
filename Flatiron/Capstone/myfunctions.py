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