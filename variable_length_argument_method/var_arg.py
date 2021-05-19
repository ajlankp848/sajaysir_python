# function to add two numbers

def add(num1,num2): #paramwters-num1,num2
    return num1+num2

res=add(10,20)  #argumets-10,20
print(res)

#to add 3 numbers
def add_three(num1,num2,num3):
    return num1+num2+num3
result=add_three(10,20,30)
print(result)

#to add 4 numbers
def add_four(num1,num2,num3,num4):
    return num1+num2+num3+num4
res=add_four(10,20,30,40)
print(res)

#instead of all these we can use
def add(*args):
    res=0
    for num in args:
        res+=num
    return res

print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,40))


def employee(**kwargs):
    for k,v in kwargs.items():
        print(k, "=>", v)
employee(id=100,nat_place="pattambbi",w_place="kochi")

