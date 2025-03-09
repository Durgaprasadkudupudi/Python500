for _ in range(int(input())):
    N=int(input())
    sum=0
    m=str(N)
    for i in m:
        sum+=int(i)
    print(sum)

for _ in range(int(input())):
    x,y=map(int,input().split())
    total=y*30
    if total>x:
        print("no")
    else:
        print("yes")