st = input()
n = int(input())
l=[]
sub_lst=[(st[i:i+n]) for i in range(0,len(st),n)]

for i in sub_lst:
    l.append(i.count('1'))
    m=max(l)

print(sub_lst)
print(m)


