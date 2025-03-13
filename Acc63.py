# cook your dish here
for _ in range(int(input())):
    w,x,y,z=map(int,input().split())
    s=x*z
    ca=w+s
    re=ca-y*z
    print(re)
    