#decorators is used , for withot modify the fn

def dec_sub(fun):
    def wrapper(num1,num2):
        if num1<num2:
            (num1,num2)=(num2,num1)
        return fun(num1,num2)
    return wrapper

@dec_sub
def sub(num1,num2):
    return num1-num2
res=sub(10,20)
print(res)