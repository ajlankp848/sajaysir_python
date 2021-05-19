employees={
    1000:{"eid":1000,"name":"ajay","salary":25000,"designation":"developer"},
    1001:{"eid":1001,"name":"vijay","salary":22000,"designation":"developer"},
    1002:{"eid":1002,"name":"sijay","salary":27000,"designation":"deve"},
    1003:{"eid":1003,"name":"nijay","salary":28000,"designation":"de"},
    1004:{"eid":1004,"name":"dijay","salary":29000,"designation":"developery"}
}
#create a function print_employee()=> calling fn print_employee(id=1000) it will name of that employee

def print_employee(**kwargs):
    id=kwargs["id"]
    prop=kwargs["prop"]
    if id in employees:
        print(employees[id]["name"])
        print(employees[id][prop])
    else:
        print("invalid id")


print_employee(id=1001,prop="salary")
#print_employee(id=1001)
#print_employee(id=1009)
