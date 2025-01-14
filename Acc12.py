# Minimum Cars required
T=int(input())
for i in range(T):
    lst=[]
    N=int(input())
    for j in range(1,N+1,4):
        lst.append(j)
    
    print(len(lst))
    
# Test Score
T = int(input())
for _ in range(T):
    N, X, Y = map(int, input().split())
    if Y % X == 0 and Y // X <= N:
        print("YES")
    else:
        print("NO")