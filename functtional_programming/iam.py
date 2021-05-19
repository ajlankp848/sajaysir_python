#functional programming is used to reduce code length
# for that we using lambda function- lambda fn is anonymous fn

#fn to add two numbers
def add(num1,num2):
    return num1+num2
r=add(10,20)
print(r)

#the above code is reducing using lambda function

ad=lambda num1,num2:num1+num2
print(ad(10,3))

#another example
def cube(num):
    return num**3
res=cube(3)
print(res)
#using lambda
cube=lambda num:num**3
re=print(cube(4))

#multiplication using lambda fn
mul=lambda num1,num2:num1*num2
res=print(mul(10,3))

#division using lambda fn
div=lambda num1,num2:num1/num2
res=print(div(10,2))


#home work
#1.list=[7,8,9,4,3,1]
#if num>5 num+1
#else num-1
#o/p is list=[8,9,10,3,2,0]
#2.list1=[10,20,21,22,23]
#list2=[20,21,10,22,23]
#check wheather these two lists are same


#there are another 3 functions
#1.map():- it is used when fn applied on each object and display o/p
#2.filter()
#3.reduce
#ex:=
list=[1,2,3,4,5]
#calculate squares of each numbers in list