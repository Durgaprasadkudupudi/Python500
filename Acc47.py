# cook your dish here

a,b,x,y=map(int,input().split())
sum1=a*2+b
sum2=x*2+y
if sum1>sum2:
    print("Messi")
elif sum2>sum1:
    print("Ronaldo")
else:
    print("Equal")

# cook your dish here
for _ in range(int(input())):
    k,x=map(int,input().split())
    total=k*7
    remaid=total-x
    print(remaid)

# cook your dish here
x=int(input())
if x<3:
    print("GOLD")
elif x>=3 and x<6:
    print("SILVER")
elif x>=6:
    print("BRONZE")

# cook your dish here
for _ in range(int(input())):
    x=int(input())
    if x>24:
        print("YES")
    else:
        print("NO")

for _ in range(int(input())):
    x,y=map(int,input().split())
    print(y//x)