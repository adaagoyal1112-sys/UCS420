print("hello world")
print("Adaa Goyal")

num1=int(input("Enter first no: "))
num2=int(input("Enter second no: "))
print(num1+num2)

str1=chr(input("Enter the first string here: "))
str2=chr(input("Enter the second string here: "))
str3=str1+str2
print(str3)

a="ferocious"
b=100
c=a+str(b)
print(c)

for i in range(11):
    print (i)

t=0
while t<=10:
    print(t)
t+=1

for n in range(1,10):
    m=n*5
print(m)

l=int(input("Enter the first no : "))
m=int(input("Enter the second no: "))
n=int(input("Enter the third no: "))
print(l+m+n)


str1=chr(input("Enter the first string here: "))
str2=chr(input("Enter the second string here: "))
str3=chr(input("Enter the second string here: "))
str4=str1+str2+str3
print(str4)

n=int(input("Enter the no here: "))
for i in range(1,10):
    print(n, "*", i, "=", n*i)

a=int(input("Enter the first no: "))
b=int(input("Enter the second no: "))
if (a>b):
    print("The biggest no : ",a)
else:
    print("The biggest no: ",b)

# no is prime or even
"""  
5.1: wap to find max among three nos and input from user
5.2: wap to add all nos f=divisible form 7 and 9 form 1 to n where n is given by user
5.3: wap to add all prime nos from 1 to n where n is given by n
"""

a=int(input("Enter the first no: "))
b=int(input("Enter the second no: "))
c=int(input("Enter the third no: "))
if(a>b):
    if(a>c):
        print(a)
    else:
        print(c)
else:
    
