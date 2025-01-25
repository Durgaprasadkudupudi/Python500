# Aircrafts
for _ in range(int(input())):
    X,N=map(int,input().split())
    res=N//100
    if X>res:
        print(0)
    elif N%100==0:
        print(res-X)
    elif N%100!=0:
        res=(res-X)+1
        print(res)

# Self Defence Training
for _ in range(int(input())):
    N=int(input())
    lst=list(map(int,input().split()))
    count=0
    for i in lst:
        if (10<=i<=60):
            count+=1
    print(count)


#Cup Finals
for _ in range(int(input())):
    X,Y,D=map(int,input().split())
    diff=abs(X-Y)
    if diff<=D:
        print("yes")
    else:
        print("No")


# Too many Floors
for _ in range(int(input())):
    X,Y=map(int,input().split())
    countX=0
    countY=0
    for i in range(1,X+1,10):
        countX+=1
    for j in range(1,Y+1,10):
        countY+=1
    print(abs(countY-countX))

# speed limit test
for _ in range(int(input())):
    A,B,X,Y=map(int,input().split())
    dis1=A/X
    dis2=B/Y
    
    if dis1==dis2:
        print("equal")
    else:
        if dis1>dis2:
            print("Alice")
        else:
            print("Bob")

#increasing Decreasing
N=int(input())
if N%4==0:
    print(N+1)
else:
    print(N-1)


def calculate_score(n, t, d):
    return max(0, n - t * d)

for _ in range(int(input())):
    X, Y = map(int, input().split())
    
    # Calculate score if A is solved first, then B
    score_AB = calculate_score(500, X, 2) + calculate_score(1000, X + Y, 4)
    
    # Calculate score if B is solved first, then A
    score_BA = calculate_score(1000, Y, 4) + calculate_score(500, X + Y, 2)
    
    # Print the maximum score
    print(max(score_AB, score_BA))



#second largest element

for _ in range(int(input())):
    a,b,c = map(int, input().split())
    lst=[]
    lst.append(a)
    lst.append(b)
    lst.append(c)
    lst.sort()
    print(lst[1])



# cook your dish here
for _ in range(int(input())):
    n,x,p=map(int,input().split())
    nattempt=n-x
    pmarks=x*3
    tmarks=pmarks-nattempt
    if tmarks>=p:
        print("Pass")
    else:
        print("Fail")
   
    
    