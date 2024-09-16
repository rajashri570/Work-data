list_people = {
    "person1" : {
        "name":"Ravi",
        "age":73,
    },
    "person2" : {
        "name":"Shiva",
        "age":25,
    },
    "person3" : {
        "name":"Sagar",
        "age":22,
    },
    "person4" : {
        "name":"Shrikant",
        "age":24,
    }
}
#Q. get the max age of person from list_people
print("type:",type(list_people))
print("nested type:",type(list_people["person1"]))
print("accessing the name of second person:",list_people["person2"]["name"])
print("No of person in list:",len(list_people))
max = 0
name = ""
for key,val in list_people.items():
    # print(f"Name:{val['name']} and Age:{val['age']}")
    if max  < val['age']:
        max = val['age']
        name = val['name']

print("Max age:",max)
print(f"{name} is having the max age-{max}")