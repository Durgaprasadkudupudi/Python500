for _ in range(int(input())):
    X, Y, N, R = map(int, input().split())
    if N * X > R:
        print(-1)
    else:
        premium_burgers = min(N, (R - N * X) // (Y - X))
        normal_burgers = N - premium_burgers
        print(normal_burgers, premium_burgers)