#covert all letters into uppercase
lst=["ajay","vijay","sajay","babu"]
def to_upper(name):
    return name.upper()
upper=list(map(to_upper,lst))
print(upper)

#using lambda fn
lst=["ajay","vijay","sajay","babu"]
upper=list(map(lambda name:name.upper(),lst))
print(upper)

#filter example

l=[2,3,4,5,6,7,89,1,55]
even=list(filter(lambda num:num%2==0,l))
print(even)


#map example
lst=[7,8,9,4,3,2]
out=list(map(lambda num:num+1 if num>5 else num-1,lst))
print(out)


#example: extract names start with a from the given list
names_list=["ajlan","adhil","shebeeb","faizy","akshay"]
names=list(filter(lambda name:name[0]=="a",names_list))
print(names)

#normal form
names_list=["ajlan","adhil","shebeeb","faizy","akshay"]
list=[]
for name in names_list:
    if name[0]=="a":
        list.append(name)
    else:
        pass
print(list)


#reduce function is used when we want only single output
#example
#in reduce we pass double parameters instead of map and filter in that we pass only one parameter
#reduce not a built in fn so first we import it
#only number can pass in reduce function method
import _functools
list=[1,2,3,4,5,6]
total=_functools.reduce(lambda num1,num2:num1+num2,list)
print(total)

#another way
from functools import reduce
list=[1,2,3,4,5,6]
total=reduce(lambda num1,num2:num1+num2,list)
print(total)

#another way
from functools import *
total=reduce(lambda num1,num2:num1+num2,list)
print(total)
highest=reduce(lambda num1,num2:num1 if num1>num2 else num2,list)
print(highest)
