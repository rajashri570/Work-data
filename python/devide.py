# write a program to divide two numbers , use function with parameter and type and also return type 
'''
Here used Optional from typing module to return None if the division is not possible
witout optional it will return None by default
but it wont give clearity of function return type ex: if only float will be there we get know that 
function will return float only which is not true if error occurs it will return None
'''
from typing import Optional
def div(num1 : int, num2: int)->Optional[float]:
    try:
        if num2 == 0:
            raise ZeroDivisionError("You can not divide by zero")
        return num1/num2
    except ZeroDivisionError as e:
        print("ERROR:",e)
print("10/0:",div(10,0)) 
print("10/2:",div(10,2))    