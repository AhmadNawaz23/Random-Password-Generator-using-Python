import random
lower = "abcdefghijklmonpqrstuvwzyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = '0123456789'
symbol = "{}[];:''/.,"
all = upper + lower + symbol
length = 9
password= "".join(random.sample(all,length))
print('Your Password is ',password)
