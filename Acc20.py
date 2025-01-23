t = int(input())
for _ in range(t):
    X, Y, Z = map(int, input().split())
    total_time = X * Y  # Total time without breaks
    if X > 3:
        # Calculate the number of breaks
        breaks = (X - 1) // 3
        total_time += breaks * Z
    print(total_time)


# cook your dish here
# Blackjack
t=int(input())
for i in range(t):
    A,B=map(int,input().split())
    tsum=21
    fres=0
    init=A+B
    if A+B>10:
        fres=tsum-init
        print(fres)
    else:
        print(-1)
        