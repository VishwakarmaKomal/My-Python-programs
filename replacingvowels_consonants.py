st1=input("enter 1st word")
st2=input("enter 2nd word")
st3=input("enter 3rd word")
vowels="aeiouAEIOU"
consonants="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
for i in  st1:
    if i in vowels:
        st1=st1.replace(i,'%')

for i in st2:
    if i in consonants:
        st2=st2.replace(i,'#')

print(st1+st2+st3.upper())





