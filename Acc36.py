
# cook your dish here
def arthematic(a,b):
    add=a+b
    subs=a-b
    mul=a*b
    div=a/b
    print("addition of two numbers:",add)
    print("substraction of two numbers:",subs)
    print("multiplication of two numbers:",mul)
    print("division  of two numbers:",div)
arthematic(25,5)

for _ in range(int(input())):
    X,Y=map(int,input().split())
    print(X*Y)



# cook your dish here
for _ in range(int(input())):
   X=int(input())
   if X==6:
       print("YES")
   else:
       print("NO")