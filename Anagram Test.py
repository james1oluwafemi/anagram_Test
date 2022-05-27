# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


first_Word = input("Enter First Word: \n")
first_Word_Strip = first_Word.strip()
first_Word_Case = first_Word_Strip.lower()
word = list(first_Word_Case)
word.sort()

second_Word = input("Enter Second Word: \n")
second_Word_Strip = second_Word.strip()
second_Word_Case = second_Word_Strip.lower()
anagram = list(second_Word_Case)
anagram.sort()


def find_anagram(word, anagram):
    # [assignment] Add your code here

    if word != anagram:
        print(False)
    else:
        print(True)

find_anagram(word, anagram)
