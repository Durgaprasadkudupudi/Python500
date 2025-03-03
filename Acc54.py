# cook your dish here
for _ in range(int(input())):
    x=int(input())
    if x<=3:
        print("BRONZE")
    elif x>3 and x<=6:
        print("SILVER")
    else:
        print("gold")

for _ in range(int(input())):
    k,n=map(int,input().split())
    score=n-k
    print(abs(score))


# cook your dish here
for _ in range(int(input())):
    x,y=map(int,input().split())
    if x==y:
        print("ANY")
    elif x>y:
        print("SECOND")
    else:
        print("FIRST")

for _ in range(int(input())):
    x=int(input())
    print(100-x)

a,b=map(int,input().split())
if a>b:
    print(a)
else:
    print(b)