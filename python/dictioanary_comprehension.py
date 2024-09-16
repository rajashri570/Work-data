#Q. write a program to create a dictionary with key as number and value as number+1

d1 ={"num1":3,"num2":7,"num3":6}
newd = {key: d1.get(key, 0) + 1 for key in d1}
print(newd)

#Q. write a program to get the value of key from dictionary if key is present else return 0
dict = {"num1":3,"num2":7,"num3":6}
try:
    print(dict.get("num8",0))
    print(dict["num5"]) #this will throw error as key is not present
except KeyError as e:
    print(f"**Error**:{str(e)}")
