'''
# Q. write a program to find out the number of occurances of each character in a string.
----------------------------------------------------------------------------------------------------------------
In this program i am first cheching if any capital letter, 
if yes then converting it to lower case.
Then i am iterating over the string and checking if the character is already present in dictionary or not.
'''



def contains_uppaercase(string):
    if any(string.isupper() for string in string):
        return True
    
# this counts the frequency of each character in a string 
def count_frequency(string):
    if contains_uppaercase(string):
        string = string.lower()
    for i in string:
        if i not in d:
            d[i] = 1
        else:
            d[i]= d[i]+1
    print("Input String: ",string)
    print("character frequency :",d)

# this counts the frequency of each word in a string
def word_count(text):
    # text_words = text.split(" ")
    if contains_uppaercase(text):
        text = text.lower()
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for word in text:
        if word in punctuation:
            text = text.replace(word,"")
    words_list = text.split(" ")
    for word in words_list:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] = word_dict[word]+1
    print(word_dict)





string = "Rajashri"
d = {}
word_dict = {}
count_frequency(string)
text = "The program waits while the user enters their response and continues after the user presses enter"
word_count(text)

