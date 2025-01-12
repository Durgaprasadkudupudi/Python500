# Reverse The Number
# cook your dish here
T=int(input())
for i in range(T):
    N=int(input())
    S=str(N)
    result=int(S[::-1])
    print(result)


# Sasta Shark Tank
# Devendra just had a million-dollar idea and he needs funds to startup. He was recently invited to Sasta Shark Tank (A TV show where entrepreneurs pitch their ideas to investors hoping to get investment in return).
T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    first_valuation = 10 * A
    second_valuation = 5 * B
    
    if first_valuation > second_valuation:
        print("FIRST")
    elif first_valuation < second_valuation:
        print("SECOND")
    else:
        print("ANY")