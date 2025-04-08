for _ in range(int(input())):
    N, S = map(int, input().split())

    maxi = 0
    for i in range(N + 1):
        j = S - i
        if 0 <= j <= N:
            k = abs(i - j)
            maxi = max(maxi, k)
    print(maxi)


def solve():
    N, S = map(int, input().split())
    print(min(S, 2 * N - S))

T = int(input())
for _ in range(T):
    solve()