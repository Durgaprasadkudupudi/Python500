for _ in range(int(input())):
    x,y=map(int,input().split())
    if x>y:
        print(x-y)
    elif y==x or x<y:
        print(0)
    
for _ in range(int(input())):
    x,y=map(int,input().split())
    print(y-x)

# cook your dish here
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    if x+y==z:
        print("YES")
    else:
        print("NO")

# cook your dish here
for _ in range(int(input())):
    x=int(input())
    if x>30:
        
        print("YES")
    else:
        print("NO")