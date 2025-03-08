for _ in range(int(input())):
    X, Y, N, R = map(int, input().split())
    if N * X > R:
        print(-1)
    else:
        premium_burgers = min(N, (R - N * X) // (Y - X))
        normal_burgers = N - premium_burgers
        print(normal_burgers, premium_burgers)


# cook your dish here
for _ in range(int(input())):
    x,y=map(int,input().split())
    if x>y:
        print("NEW PHONE")
    elif y>x:
        print("REPAIR")
    else:
        print("ANY")