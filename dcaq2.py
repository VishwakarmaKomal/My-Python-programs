st=input()
l=[]
s=""
count=0
for i in range(0,len(st)):
    if st[i]=='H':
        for j in range(i+1,len(st)):
            if st[j]=='S':
                for k in range(j+1,len(st)):
                    if st[k]=='L':
                        s=st[i]+st[j]+st[k]
                        count+=1
                        l.append(s)
print(l)
print(count)









