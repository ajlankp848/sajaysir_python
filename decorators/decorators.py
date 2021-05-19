#substractiob of two numbers

def sub(num1,num2):
    return num1-num2
res=sub(10,5)
print(res)
#if we inagne kodthal
resu=sub(5,10)
print(resu) #we get negative answer

#to avoid negative answer we want subtract lowest value from highest value to do that
#we modify the function.
def subtract(num1,num2):
    if num1<num2:
        (num1,num2)=(num2,num1)
    return num1-num2
result=subtract(12,6)
resulta=subtract(6,13)
print(result)
print(resulta)

#without any modification we can done this by
#decorators is used to add any features to our function without modify that function
