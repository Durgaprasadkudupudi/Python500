# cook your dish here
t=int(input())
for _ in range(t):
    N,K,M=map(int,input().split())
    pocket=0
    bag=0
    for i in range(1,N+1,M):
        pocket+=1

    for j in range(1,pocket+1,K):
        bag+=1
    print(bag)
        


t = int(input())
for _ in range(t):
    X, Y = map(int, input().split())
    if Y > X:
        print(X)
    else:
        # Calculate the number of full Y steps
        full_steps = X // Y
        # Calculate the remaining steps
        remaining_steps = X % Y
        # Total moves = full_steps + remaining_steps
        print(full_steps + remaining_steps)


# cook your dish here
t=int(input())
for _ in range(t):
    X1,X2,Y1,Y2=map(int,input().split())
    a=abs(X1-Y1)
    b=abs(X2-Y2)
    print(abs(max(a,b)))
    
    
# cook your dish here
for _ in range(int(input())):
    x,y=map(int,input().split())
    count=0
    if x<y:
        print(0)
    else:
        # for j in range(1,x+1,y):
        #     count+=1
        print(int(x/y))
    
    # Water Mixing
for _ in range(int(input())):
    A,B,X,Y=map(int,input().split())
    if A==B:
        print("YES")
    elif B>A:
        res=B-A
        if X>=res:
            print("YES")
        else:
            print("NO")
    elif A>B:
        res=A-B
        if Y>=res:
            print("YES")
        else:
            print("NO")

# Weights
for _ in range(int(input())):
    W,X,Y,Z=map(int,input().split())
    if X==W or Y==W  or Z==W:
        print("YES")
    elif W==X+Y or W==Y+Z or W==Z+X:
        print("YES")
    elif W==X+Y+Z:
        print("YES")
    else:
        print("NO")


# Chef and his Apps
for _ in range(int(input())):
    S,X,Y,Z=map(int,input().split())
    stored=X+Y
    space= S-stored
    lst=[X,Y]
    lst.sort()
    if space>=Z:
        print(0)
    elif space<Z:
        lst.remove(lst[1])
        stored=lst[0]
        space=S-stored
        if space>=Z:
            print(1)
        else:
            print(2)


# Chef Eren
for _ in range(int(input())):
    N,A,B=map(int,input().split())
    ocount=0
    ecount=0
    sum=0
    for i in range(1,N+1):
        if i%2==0:
            ecount+=1
        else:
            ocount+=1
    ecount=ecount*A
    ocount=ocount*B
    sum=(ecount+ocount)
    print(sum)
        
        
# 5,10 coins
for _ in range(int(input())):
    X = int(input())

    if X % 5 != 0:
        print(-1)
    else:
        tcount = X // 10  # Count of 10s in X
        remainder = X % 10  # Remaining value after taking 10s

        if remainder == 0:
            print(tcount)
        else:
            fcount = remainder // 5  # Count of 5s in the remainder
            print(tcount + fcount)

    