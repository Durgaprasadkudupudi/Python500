# Endless Appetizers
for _ in range(int(input())):
    X,Y,R=map(int,input().split())
    sticks=0
    plates=0
    for i in range(1,R,30):
        sticks+=1
    total=X+sticks
    
    for j in range(1,total+1,Y):
        plates+=1
    print(plates)
    

# Presents for Cheffina
for _ in range(int(input())):
    N = int(input())
    free_gifts = N // 5
    coins = N - free_gifts
    print(coins)    


# factorial
for _ in range(int(input())):
    N=int(input())
    fact=1
    for i in range(1,N+1):
        fact=fact*i
    print(fact)

# Dracula Eats
for _ in range(int(input())):
    N=int(input())
    days=0
    for i in range(1,N,7):
        days+=1
    print(days)


# Possible Victory
R,O,C=map(int,input().split())
oversleft=(20-O)*6
max_score=oversleft*6
total=C+max_score
if total>R:
    print("Yes")
else:
    print("No")

