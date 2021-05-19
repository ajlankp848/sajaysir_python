#if we want divide highest by lowest

def dec_div(fun):
    def wrapper(num1,num2):
        if num1<num2:
            (num1,num2)=(num2,num1)
        return fun(num1,num2)
    return wrapper
@dec_div
def div(num1,num2):
    return num1/num2
res=div(2,10)
print(res)

@dec_div
def add(num1,num2):
    return num1+num2
ad=add(10,50)
print(ad)

@dec_div
def sub(num1,num2):
    return num1-num2
su=sub(9,17)
print(su)