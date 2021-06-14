from array import *
n = int(input("enter the size of list"))
l1 = []
count = 0
for i in range(n):
    e = input()
    l1.append(e)
print(l1)
k=1
for j in range(0,len(l1),k+1):
    if l1[j] == 'P' or l1[j] == 'T':
        for m in range(j+1,len(l1)):

            if l1[m] == 'T' or l1[m] == 'P':
                count += 1
            break
print(count)







