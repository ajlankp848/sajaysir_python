list1=[7,8,9,4,3,1]
list=[]
for i in list1:
    if i>5:
        i+=1
        list.append(i)

    else:
        i-=1
        list.append(i)
print(list)

#it can also write in this form below
list1=[7,8,9,4,3,1]
out=[]
for i in list1:
    out.append(i+1) if i>5 else out.append(i-1)
print(out)

#using map functtion

lst=[7,8,9,4,3,1]
op=map(lambda num:num+1 if num>5 else num-1,lst)
print(op)

#example of filter fn
#find even numbers from given list

lst=[1,3,2,4,5,6,7,8]
op=filter(lambda num:num%2==0,lst)
print(op)