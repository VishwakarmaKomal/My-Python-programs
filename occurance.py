str=input("enter string")
n=len(str)
#ch=str[0]

for i in range(0,n):
    for j in range(i+1,n):
        if str[i]==str[j]:
            ch=str[j]
            str=str.replace(ch,'$')

print(str)

'''for i in str:
    if i==ch:
        str=str.replace(ch,'$')
print(str)'''


