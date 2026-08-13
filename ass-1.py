# %% hello world
print ("hello world")

# %% Add 2 nos
a=10
b=220
c=a+b
print(a, "+", b, "=", c)

# %% concatenate strings
a="Bhagat"
b=" Singh"
c=a+b
print(c)

# %% concatenate string with number
a="Bhagat"
b= 100
c=a+str(b)
print(c)

# %% add 3 nos
a=1
b=2
c=3
d=a+b+c
print("d =",d)

# %% concatenate 3 strings 
a="Adaa"
b=" Goyal"
c=" Engineer"
d=a+b+c
print(d)

# %%input 2 strings and concatenate
a=input("Enter first string: ")
b=input("Enter second string: ")
c=a+b
print(c)

# %%input 2 nos from user and add
a= int(input("Enter first no: "))
b= int(input("Enter second no: "))
c=a+b
print(c)

# %% while loop
i=1
while i<=10:
    print(i)
    i=i+1

# %% range func
print("Range(10): ", list(range(10)))
print("Range(10,20): ", list(range(10,20)))

# %% for loop
for i in range(0,10):
    print(i)

# %% for loop
for i in range(0, 20, 2):
    print(i)

# %% for loop
for i in range(0, -10, -1):
    print(i)

# %% table of 5
for i in range(1,11):
    print(i ,"* 5 = ",i*5)

# %% sum of all nos from 1-10
i=1
s=0
while i<=10:
    s=s+i
    i=i+1
print(s)


# %% sum using for loop
s=0
for i in range(1,11):
    s=s+i
print(s)

# %% using sum func
print("Sum is : ", sum(range(1,11)))

# %% del sum to make sum func work
del sum

# %% print table of 7
for i in range(1,11):
    print("7 *", i ,"=", 7*i)

# %% table of 9
i=1
while i<=10:
    print("9 * ",i ,"= ",9*i)
    i=i+1

# %% pritn table of n given by user
n=int(input("Enter the no: "))
i=1
while i<=10:
    print(n," * ",i ,"= ",n*i)
    i=i+1

# %% add all no from 1 to n given by user
n= int(input("Enter no: "))
print("Sum: ", sum(range(1,n+1)))

# %% if else
a= int(input("Enter a: "))
b= int(input("Enter b: "))
if a>b:
    print(a)
else:
    print(b)


# %% no is odd or even
n= int(input("Enter no: "))
if n%2==0:
    print("even")
else:
    print("odd")

# %% prime nos
n= int(input("Enter no: "))
f=0
for i in range(2, n//2+1):
    if n%i ==0:
        f=1
        break
if f==0:
    print("prime")
else:
    print("Composite")

# %% compare strings
a= input("Enter string a: ")
b= input("Enter string b: ")
if a==b:
    print("a==b")
elif a>b:
    print("a")
else:
    print("b")

# %% max among 3 nos
a= int(input("Enter a: "))
b= int(input("Enter b: "))
c= int(input("Enter c: "))
print("Max: ",max(a,b,c))

# %% add all nos divisible by 7 and 9
n= int(input("Enter no: "))
s=0
for i in range(1,n+1):
    if i%7==0:
        if i%9==0:
            s=s+i
print(s)

# %% add all prime nos from 1 to n
n= int(input("Enter no: "))
s=0
for i in range(1,n+1):
    for j in range(1,i//2+1):
        if i%j==0:
            s=s+i
print(s)
# %% func dec
def Add(a,b):
    c=a+b
    return c
print("Add(10,20)= ",Add(10,20))

# %% prime no func
def prime(n):
    for i in range (1, n//2+1):
        if n%i==0:
            return 0
    return 1
print(prime(20))

# %% 
