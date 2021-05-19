#list comprehension
#find squares of all elements in list and store in another list
#normal form

list=[2,3,4,5]
squares=[]
for num in list:
    s=num**2
    squares.append(s)
print(squares)

#using list comprehension
list=[2,3,4,5,6]
squares=[num**2 for num in list]
print(squares)

#another example, we want output in pairs of each fruit
fruits=["apple","orange","mango"]
pairs=[(fruit,fruit) for fruit in fruits]
print(pairs)

#example2,
list1=[1,2]
list2=[10,20]
#we want op [(1,10),(1,20),(2,10),(2,20)]
pairs=[(num1,num2) for num1 in list1 for num2 in list2]
print(pairs)

#example3
list=[10,11,12,13,14]
even=[num for num in list if num%2==0]
print(even)

#example4
list=[7,8,9,4,3,2]
pattern=[num+1 if num>5 else num-1 for num in list]
print(pattern)



