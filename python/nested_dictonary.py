#write a program to create company object of dict type and add different employees by department to it

Comapny = {
    "IT" : {
        "employee1" : {
            "name":"Ravi",
            "age":23,
            "salary":50000
        },
        "employee2" : {
            "name":"Shiva",
            "age":25,
            "salary":60000
        },
        "employee3" : {
            "name":"Sagar",
            "age":22,
            "salary":40000
        }
    },
    "HR" : {
        "employee1" : {
            "name":"Shrikant",
            "age":24,
            "salary":30000
        },
        "employee2" : {
            "name":"Radhe",
            "age":26,
            "salary":70000
        }
    }
}
print("sal of employee1 in HR:",Comapny['HR']['employee1']['salary'])
print("Company:",Comapny)
print("---Employess in IT department:---")
for key,val in Comapny["IT"].items():
    print(f"Name:{val['name']} Age:{val['age']} Salary:{val['salary']}")