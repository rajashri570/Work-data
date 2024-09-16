'''
Start with your program from Exercise 3-6. Add a new line that prints a 
message saying that you can invite only two people for dinner.
•	 Use pop() to remove guests from your list one at a time until only two 
names remain in your list. Each time you pop a name from your list, print 
a message to that person letting them know you’re sorry you can’t invite 
them to dinner.
•	 Print a message to each of the two people still on your list, letting them 
know they’re still invited.
•	 Use del to remove the last two names from your list, so you have an empty 
list. Print your list to make sure you actually have an empty list at the end 
of your program
'''
l = ["ravi","shrikant","shiva","anjali","girija","sumna"]
for i in l:
    print(f"Inviting for dinner: {i}")

while len(l) > 2:
   
    name = l.pop()
    print(f"Sorry,plan changed going but so cant invite you for dinner: {name}")
if len(l) <= 2:
    print(f"{l[0]} and {l[1]} are invited for dinner")

del l[:]
print(l)

# Sorting a list permanently with the sort() method

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("---------Original order---------")
print(cars)
cars.sort()
print(cars)

# Sorting a list permanently in reverse alphabetical order with sort() method
print("---------Reverse order---------")
name = ["apple","banana","mango","grapes"]
print(name)
cars.sort(reverse=True)
print(cars)
#sorted function is used to sort the list temporarily original list will not be changed
loaction = ["pune","mumbai","Banglore","nashik"]
print("---------Original order---------")
print(loaction)
print("---------Sorted order---------")
print(sorted(loaction))
print("---------Original order---------")
print(loaction)
