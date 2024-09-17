list1 = [22,33,55,66]
print("list:",list1)
del list1[2]  # deleted using the del keyword

print("updated list:",list1)
pop_item_last = list1.pop()
print("poped item:",pop_item_last)
print("updated list:",list1)
pop_item_first = list1.remove(1)
print("poped item:",pop_item_first)