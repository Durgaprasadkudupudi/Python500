# Reach fast
for _ in range(int(input())):
    A,B,K=map(int,input().split())
    steps=0
    if A==B:
        print(0)
    elif A>B:
        for i in range(B,A,K):
            steps+=1
        print(steps)
    elif B>A:
        for j in range(A,B,K):
            steps+=1
        print(steps)


#Single-use Attack
for _ in range(int(input())):
    H,X,Y=map(int,input().split())
    remaining=H-Y
    steps=0
    for i in range(1,remaining+1,X):
        steps+=1
    print(steps+1)


# Get Lowest Free
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    offer=min(a,b,c)
    total=a+b+c
    paid=total-offer
    print(paid)


# Minimum number of Flips
for _ in range(int(input())):
    N = int(input())
    lst = list(map(int, input().split()))
    
    sump = sum(1 for i in lst if i > 0)  # Count positive numbers
    sumn = sum(1 for i in lst if i < 0)  # Count negative numbers

    # If already balanced
    if sump == sumn:
        print(0)
    
    # If there are no negative numbers
    elif sumn == 0:
        if N % 2 == 0:
            print(N // 2)  # Convert half of them to negative to balance
        else:
            print(-1)  # Impossible to balance an odd-length list with only positives

    # If the counts are not equal
    else:
        if N % 2 != 0:  # If length is odd, balancing is impossible
            print(-1)
        else:  # Length is even, calculate required changes
            print(abs(sump - sumn) // 2)  # Half the difference needs to be flipped  