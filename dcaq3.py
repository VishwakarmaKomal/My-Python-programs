s=set(input("enter the elements of set"))
print(s)
l=[]
l2=[]
n=int(input("enter the size of list"))
for i in range(n):
    l.append(input())
print("Original List:",l)
for i in l:
    if i=='1':
        l2.append(i)
for i in l:
    if i=='0':
        l2.append(i)
for i in l:
    if i=='2':
        l2.append(i)
print("Expected Output:",l2)





