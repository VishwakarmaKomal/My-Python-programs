n = int(input("Enter the n"))
#st = input("enter a string")
def string_large(str,n):
    result_string = ""
    if n <= 0:
        print(f" invalid input {n}")

    if n > 0:
        for i in range(n):
            result_string = result_string+str
    return result_string

st = input("enter a string")
print(string_large(st,n))






