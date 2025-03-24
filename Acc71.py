import math
for _ in range(int(input())):
    n,x=map(int,input().split())
    res=math.ceil(n/6)
    print(res*x)