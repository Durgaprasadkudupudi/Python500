# Qualify the round
# In a coding contest, there are two types of problems:

# Easy problems, which are worth 
# 1
# 1 point each
# Hard problems, which are worth 
# 2
# 2 points each

T=int(input())
for i in range(T):
    X,A,B = map(int,input().split())
    total=A+B*2
    if total>=X:
        print("Qualify")
    else:
        print("NotQualify")


# Elections in Chefland
# Election season has started in Chefland and the election commission wants to know the count of eligible voters.
# cook your dish here
T=int(input())

for i in range(T):
    count=0
    N,X=map(int,input().split())
    
    lst=list(map(int,input().split()))
    for j in lst:
        if j>=X:
            count+=1
    print(count)