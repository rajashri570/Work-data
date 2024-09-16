l  = ["radhe","shiva","sagar","shrikant"]
print("List of name:",l)
try:
    print(l[4])
except IndexError as e:
    print(f"**Error**:{str(e)}")
print("End of program")



print("-----------------Ternery Operator-----------------")
age = 56
if age < 4:
 price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 9
print(f"Your admission cost is ${price}.")