#1.write a program to show woring of ternery operator
print("-----------------Ternery Operator-----------------")
num = 10
result = 'even' if num%2==0 else 'odd'
print(f"{num} is {result}")
print("--other way of cheking even or odd--")
num = 11
result2 = ("odd","even")[num%2==0]   # (if false, if true)[condition]
print(f"{num} is {result2}") 


  
