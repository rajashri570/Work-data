#Q.write a program to swap the keys and values of dictionary
dict = {"name":"rajashi","age":23}
inverted_dict = {}

for key,val in dict.items():
    inverted_dict[val] = key
    print(key,val)
print(inverted_dict)