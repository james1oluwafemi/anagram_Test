

def read_file_content(filename):
     f = open('story.txt','r')
     words = f.read()
     print(words)
     f.close()

read_file_content("story.txt")


def count_words():
     text = read_file_content("./story.txt")
     for char in '?., \n':
          text=text.replace(char,' ')
     text = text.lower()
     word_list = text.split()
     
     d={}
     for word in word_list:
          d[word] = d.get(word, 0) + 1

print(count_words())
