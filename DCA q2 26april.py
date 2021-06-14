from array import *

n=int(input("enter the size of array"))
arr=array('i',[])
ar=array('i',[])
for i in range(n):
    arr.append(int(input()))
print(arr)
for i in range(len(arr)-1):
    sum=0
    for j in range(i+1,len(arr)):
        sum+=arr[j]
    ar.append(sum)
#ar.append(0)
print(ar)




