for _ in range(int(input())):
    n,x,k=map(int,input().split())
    money=n*x
    if money<=k:
        print("YES")
    else:
        print("NO")

for _ in range(int(input())):
    x,y=map(int,input().split())
   
    if x>y:
        print("YES")
    else:
        print("NO")

# cook your dish here
for _ in range(int(input())):
    x1,y1,x2,y2=map(int,input().split())
    first=x1+y1
    sec=x2+y2
   
    if first>sec:
        print(sec)
    else:
        print(first)

for _ in range(int(input())):
    x=int(input())
    if x<=300:
        print(300*10)
    else:
        print(x*10)