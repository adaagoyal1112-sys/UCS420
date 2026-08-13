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

# %%
