# Q. write a program to convert the list of string to uper case using lambda function.

list1 = ["rajashri","suraj","shravani","lina"]

list2 = list(map(lambda x:x.upper(),list1)) #as map will returns the map object so we need to convert it to list
print("Newly created list:",list2)