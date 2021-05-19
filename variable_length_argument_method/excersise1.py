#to add numbers using function
#single * tuple form
def add(*args):
    res=0
    for num in args:
        res+=num
    return res
print(add(10,20))
print(add(1,2,3,45)) #so on.........