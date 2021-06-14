def getstring(str):
    if len(str)<2:
        return ""
    else:
        return str[:2]+str[-2:]
str=input("enter the string")
print("Result string:",getstring(str))