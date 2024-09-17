list1 = [3,[5,6],7,[2,[3,[5]],8],9]
new_list = []
def flatten_list(list1):
    for i in list1:
        if isinstance(i,list):
            flatten_list(i)
        else:
            new_list.append(i)

print("Original list:",list1)
print("Flatten list:")
flatten_list(list1)
print(new_list)

# #another methos use numpy flatten
# import numpy as np
# nl = np.array(list1).flatten()
# print(nl)


        