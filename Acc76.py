# cook your dish here
import math
for _ in range(int(input())):
    n,x=map(int,input().split())
    slides=n*x
    print(math.ceil(slides/4))


#printing name n times using recursion
def fun(i,n):
    
    if i>n:
        return 
    print("Balu")
    fun(i+1,n)
n=int(input("enter n value:"))
fun(1,n)


#printing 1-n using recursion
def fun(i,n):
    
    if i>n:
        return 
    print(i,end=' ')
    fun(i+1,n)
n=int(input("enter n value:"))
fun(1,n)