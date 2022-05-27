str1 = input("First Word: ")
str2 = input("Second word: ")

def find_anagram(str1, str2):

    str1 = sorted(str1)
    str2 = sorted(str2)

    if str1 == str2:
        return True
    else:
        return False


print(find_anagram(str1, str2))
