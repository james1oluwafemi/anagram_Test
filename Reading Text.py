# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
     f = open('story.txt','r')
     print(f.read())
     f.close()

read_file_content("story.txt")


def count_words():
    text = read_file_content("./story.txt")
    words = f.split()
    number_of_words += len(words)
    print(number_of_words)
##
##count_words()

    

    # [assignment] Add your code here
    #return {"as": 10, "would": 20}
