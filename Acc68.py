for _ in range(int(input())):
    c,x,y=map(int,input().split())
    if c==x:
        print(0)
    elif c>x:
        rem=(c-x)*y
        print(rem)
    elif x>c:
        print(0)

for _ in range(int(input())):
    a,b,c,x=map(int,input().split())
    if a+b>=x or b+c>=x or c+a>=x:
        print("yes")
    else:
        print("No")


for _ in range(int(input())):
    x,y,z=map(int,input().split())
    if x+y<=z:
        print(2)
    elif x<=z:
        print(1)
    else:
        print(0)