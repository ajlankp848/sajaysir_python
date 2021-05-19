array=[2,3,4,5,6]
#find squares of each number and store
#normal method
arr=[]
for i in array:
    i=i**2
    #print(i)
    arr.append(i)
print(arr)

#using map function
arr=[2,3,4,5,6]
def square(num):
    return num**2
square_list=list(map(square,arr))
print(square_list)

#using lambda function
arr=[2,3,4,5,6]
square_list=list(map(lambda num:num**2,arr))
print(square_list)