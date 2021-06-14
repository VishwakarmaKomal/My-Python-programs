def power(base,exp):
    if exp==0 or exp==1:
        return base
    if exp!=1:
        return (base*power(base,exp-1))

base=int(input("enter the base number:"))
exp=int(input("enter the exponent value:"))
print("Result:",power(base,exp))
