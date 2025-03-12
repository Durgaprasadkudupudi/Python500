# cook your dish here
for _ in range(int(input())):
    x,y=map(int,input().split())
    print(min(x,y))

for _ in range(int(input())):
    x,y,z=map(int,input().split())
    total_seets=x*10
    if total_seets>=y:
        print(y*z)
    else:
        print(total_seets*z)

# cook your dish here
x=int(input())
t=7+x
if t>170:
    print("yes")
else:
    print("No")

for _ in range(int(input())):
    x=int(input())
    if x>15:
        print("NO")
    else:
        print("YES")
