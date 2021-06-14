import random
import array
max_length = 12
lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z']
upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
digit = [0,1,2,3,4,5,6,7,8,9]
special_ch = ['@','!','#','$','%','{','&','*','(',')','<','>']

random_lower = str(random.choice(lower))
random_upper = str(random.choice(upper))
random_digit = str(random.choice(digit))
random_ch = str(random.choice(special_ch))
combined = str(lower+upper+digit+special_ch)

temp_pswd = random_ch+random_digit+random_upper+random_lower
#print(temp_pswd)
for i in range(max_length-4):
    temp_pswd = temp_pswd + random.choice(combined)
    temp_pass_list = array.array('u',temp_pswd)
    random.shuffle(temp_pass_list)

password=""
for x in temp_pass_list:
    password = password+x
print(password)


