#format of list comprehension
#list_using_comp = [var for var in input_list if var % 2 == 0]
x=1
y=1
z=2
n=3
i=0
j=0
k=0
inputlist=[]
for i in range(x+1):

    for j in range(y+1):
        for k in range(z+1):
            a=[]
            a.append(i)
            a.append(j)
            a.append(k)
            inputlist.append(a)
print(inputlist)

#print only those where sum of i, j, k is not equal to n(which is 3)
outputlist=[[[[i, j, k] for k in range(z+1) if i+j+k!=n] for j in range(y+1)] for i in range(x+1) ]
'''outputlist=[]
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k!=n:
                b=[]
                b.append(i)
                b.append(j)
                b.append(k)
                outputlist.append(b)'''
print(outputlist)







