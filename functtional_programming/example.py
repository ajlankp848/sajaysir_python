#slove the following questions uing given data set
#1.print employee names only map
#2.print all empolyee name in uppercase map
#3.print employee details whose name start with a filter
#4.print employee details whosw salary>23000 filter
#5.print employee details whose designation is developer


employees=[
    {"eid":1000,"name":"ajlan","salary":25000,"designation":"developer"},
    {"eid":1001,"name":"adhil","salary":30000,"designation":"mechanic"},
    {"eid":1002,"name":"shebeeb","salary":25000,"designation":"advisor"},
    {"eid":1003,"name":"minhal","salary":32000,"designation":"developer"},
    {"eid":1004,"name":"tibin","salary":35000,"designation":"developer"}

]
e_name=list(map(lambda name:name["name"],employees))
print(e_name)

upper_name=list(map(lambda name:name.upper(),e_name))
print(upper_name)

e_details=list(filter(lambda name:name["name"][0]=="a",employees))
print(e_details)

ed=list(filter(lambda emp:emp["salary"]>30000,employees))
print(ed)

developers=list(filter(lambda emp:emp["designation"]=="developer",employees))
print(developers)

#print the developer's details whose salary>26000
dev=list(filter(lambda emp:emp["designation"]=="developer" and emp["salary"]>26000,employees))
print(dev)

#to print highest salary from above data
from functools import reduce
high_sal=reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,
                list(map(lambda emp:emp["salary"],employees)))
print(high_sal)

#print employee names only using list comprehension
e_name=[emp["name"] for emp in employees]
print(e_name)

#print names in upper using list comprehension
e_name_upper=[emp["name"].upper() for emp in employees]
print(e_name_upper)

#print employee details whose name start with a using comprehension
emp_name=[emp["name"] for emp in employees if emp["name"][0]=="a"]
print(emp_name)

#4.print employee details whosw salary>23000 using list comprehension
empl=[emp for emp in employees if emp["salary"]>28000]
print(empl)


