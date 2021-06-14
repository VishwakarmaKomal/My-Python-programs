def check_length(nu):
    l=0
    while(nu != 0):
        l=l+1
        nu=nu//10
    return l

num=175
n=num
rem=sum=0
length=check_length(num)


while(num>0):
    rem=num%10
    sum=sum+(rem**length)
    num=num//10
    length-=1

if(sum==n):
    print(f'{n} is disarium number')
else:
    print(f'{n} is not disarium number')

