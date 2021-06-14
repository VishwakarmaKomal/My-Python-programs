def check_password(str1):
    n = len(str1)
    digit = "0123456789"
    if str1[0] == digit:
        return 0
    for i in range(n):
        if str1[i] == " " or str1[i] == "/":
            return 0
    for i in str1:
        if i.isupper():
            pass
        if i.isdigit():
            pass
    for i in range(n):
        count = 0
        if i != "":
            count += 1
    if count < 4:
        return 0
    else:
        return 1

str = input("enter Password")
print(check_password(str))





