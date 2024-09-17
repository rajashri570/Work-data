# Q.write a program to sort the list of tuple in python.
#input -  [("Alice", 30), ("Bob", 25), ("Charlie", 35)]

def sort_tuple(list1):
    l = len(list1)
    for i in range(l):
        for j in range(l-1-i):
            if list1[j][0] > list1[j+1][0]:
                list1[j],list1[j+1] = list1[j+1],list1[j]
    return list1
l = sort_tuple([("Alice", 30), ("Romi", 25), ("Charlie", 35)])
print(l)
    

