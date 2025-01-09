#Find the Fibonacci Series up to Nth Term in Python
n= 6
a=0
b=1
print(a,b,end =" ")
for i in range (0,n):
    c=a+b
    a=b
    b=c
    print(c, end= " ")
print()


