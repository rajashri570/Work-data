l = ["listen", "silent", "enlist", "hello", "world","lohel"]
anagram_dict = {}
not_anagram = {}

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if(len(l[i])==len(l[j])):
            if(sorted(l[i])==sorted(l[j])):
                print(sorted(l[i]),sorted(l[j]))
                anagram_dict[l[i]] = l[j]
                print(l[i],":",l[j])
            else:
                not_anagram[l[i]] = l[j]
print("Anagram words:",anagram_dict)
print("Not Anagram words:",not_anagram)

'''
logic used :
1. take a list of words
2. two loops i am using to compare each word with other word
3.first i loop will start 0-3
4. second loop will start (i+1) - 4
5. in first iteration i = 0 and j =1
6. compares the "listen" and "silent" and checks if both are anagram
7. next comapres listem and enlist ....
8. cheking first length of two equals 
9. then sorting the two words and comparing if both are equal
'''