list1 = ["listen", "silent", "enlist", "hello", "world","lohel"]
anagram_dict = {}
not_anagram = {}
an = {}

print("Original list:",len(list1))

for i in range(len(list1)):
    print("i:",i)
    for j in range(i+1,len(list1)):
        print("j:",j)
        if(len(list1[i])==len(list1[j])):
            if(sorted(list1[i])==sorted(list1[j])):
                print(sorted(list1[i]),sorted(list1[j]))
                anagram_dict[list1[i]] = list1[j]
                print(list1[i],":",list1[j])
            else:
                not_anagram[list1[i]] = list1[j]
        else:
            print("--------------")
            an[list1[i]] = list1[j]
            print(f"-------------asasas-------------- {list1[i]} : {list1[j]}")
print("Anagram words:",anagram_dict)

print("Not Anagram words:",not_anagram)
print("Anagram------------------------ words:",an)

