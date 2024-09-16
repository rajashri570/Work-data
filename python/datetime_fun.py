import datetime
from dateutil import parser   # to convert any date string to date object
from datetime import timedelta

# 1. Write a Python program to display the current date and time.

current = datetime.datetime.now()
print("Current time and date: ", current)
print("-"*30)

# 2. Write a Python program to convert a string to datetime.

today = str(datetime.datetime.now().date()) 
print("Today's date: ", today)
print("-"*30)

# 3. Write a Python program to subtract five days from current date.
fifthday = datetime.datetime.now().date() + timedelta(days=5)
print("fifth day from today:",fifthday)
print("-"*30)

# 4. Write a Python program to print yesterday, today, tomorrow.
yesterday = datetime.datetime.now().date() - timedelta(days=1)
tomorrow = datetime.datetime.now().date() + timedelta(days=1)   
print("Yesterday: ",yesterday)
print("Today: ",datetime.datetime.now().date())
print("Tomorrow: ",tomorrow)
print("-"*30)

# 5. get the date from user in string format and convert ito the date format
date_input = input("Enter the date in any format : ")
# date = datetime.datetime.strptime(date_input, "%Y-%m-%d")
# 
date_obj = parser.parse(date_input)
print("date in date format: ", date_obj)
print("type if date_obj: ", type(date_obj))
print("-"*30)

# 6. get the date from user in string format and convert ito the date format
date_input2 = input("Enter the date in format: dd-mm-yyyy : ")
date_obj2 = datetime.datetime.strptime(date_input2, "%d-%m-%Y")
print("take date in given format and converted to date obj:",date_obj2)
print("-"*30)



