for _ in range(int(input())):
    x,y=map(int,input().split())
    if x==y:
        print(0)
    elif x>y:
        print(0)
    else:
        print(y-x)

for _ in range(int(input())):
    x,y,z=map(int,input().split())
   
    print(x*y*z)

for _ in range(int(input())):
   n=int(input())
   print(n*2)

# cook your dish here
for _ in range(int(input())):
    n=int(input())
    if 1<=n<=4:
        print("YES")
    else:
        print("NO")
    
for _ in range(int(input())):
    x,y=map(int,input().split())
    if x<y*2:
        print("NO")
    else:
        print("YES")

for _ in range(int(input())):
    x,y,z=map(int,input().split())
    print(x-y+z)