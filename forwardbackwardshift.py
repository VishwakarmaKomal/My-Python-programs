s1 = input("enter a string")
fs = ""
bs = ""
fs = s1[-1]+s1[:-1]
bs = s1[1:]+s1[0]
print(fs)
print(bs)
if fs == bs:
    print(1)
else:
    print(0)

