#Q.write a program to merger the two dictionary into one

dict1 = {"name":"rajashi","age":23}
dict2 = {"city":"pune","state":"MH"}
for key,val in dict2.items():
    dict1[key] = val
print("merged:",dict1)

dict1 = {'apple': 5, 'banana': 8, 'orange': 12}
dict2 = {'banana': 4, 'orange': 7, 'grape': 10}

# Merge with sum of common keys
merged_dict = {key: dict1.get(key, 0) + dict2.get(key, 0) for key in set(dict1) | set(dict2)}

print(merged_dict)
