n=int(input("enter the number of days"))
l1=[]
out=[1]
output=""
for i in range(0,n):
    e=int(input())
    l1.append(e)
l = len(l1)
for i in range(1,l):

    if l1[i]<l1[i-1]:
        out.append(1)
    elif l1[i]>l1[i-1] and l1[i]<l1[i-2]:
        out.append(2)
    elif l1[i]>l1[i-1] and l1[i]>l1[i-2] and l1[i]<l1[i-3]:
        out.append(4)
    elif l1[i]>l1[i-1] and l1[i]>l1[i-2] and l1[i]>l1[i-3]and l1[i]<l1[i-4]:
        out.append(1)
    else:
        out.append(5)
print(out)







