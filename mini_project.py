import random as rd

letters="abcdefghijklmnopqrstuvwxyz"
digits="0123456789"
sym="!@#$%^&*()"

print("How many letters do you want: ")
l=int(input())
print("How many digits do you want: ")
d=int(input())
print("How many symbols do you want: ")
s=int(input())

password=""
for i in range(l):
    password+=rd.choice(letters)
for i in range(d):
    password+=rd.choice(digits)
for i in range(s):
    password+=rd.choice(sym)
password="".join(rd.sample(password,len(password)))


print("Your password is: "+password)
