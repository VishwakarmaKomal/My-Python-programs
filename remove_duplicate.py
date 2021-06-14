s = input("enter a string")
n=len(s)
s1=list(s)
l=len(s1)
#j=l-1
k=1
'''for i in range(j):
    if s[i] == s[j]:
        s=s[::-1]'''
i=0
j=1
while i<n:
    while j<n+1:
        if s[i]==s[j]:
            s1.remove(s1[i])

            i+=1
            j+=1
        else:
            i=i+1
            j+=1
print(s1)









