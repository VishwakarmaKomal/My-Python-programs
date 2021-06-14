from array import *
n=4
a1=array('i',[11,9,12])
print(a1)
l=list(a1)
m=len(l)

for i in range(m-1,-1,-1):
    for j in range(i-1,-1,-1):
        if l[i]<l[j]:
            break
        if i == m-1:
            continue
    if i==1:
        print(-1)
        break
    elif i!=m-1:
        for e in range(i,m-1):
            if l[e]>l[e+1]:
                continue
        print(l[e])
        break


'''out=-1
i=0
j=1
while i<n and j<=n:
    if  a1[j]>a1[i] and a1[j]<a1[j+1]:
        out=a1[j]
    i+=1
    j+=1

print(out)'''



