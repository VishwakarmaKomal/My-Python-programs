v = input("enter virus composition")
n = int(input("enter the number of people"))
l1 = []
l = len(v)
flag=0
for i in range(n):
    p = input()
    l1.append(p)
for j in l1:
    st = j
    l2 = len(st)
    i=0
    k=0
    while i<l2 and k<l:
        if st[i] == v[k]:
            i=i+1
        k=k+1
    if i == l2:
        print("positive")
    else:
        print("negative")

















