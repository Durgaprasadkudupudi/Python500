# ATM machine codechef problem
for _ in range(int(input())):
    N,K=map(int,input().split())
    s=''
    lst=list(map(int,input().split()))
    for i in lst:
        if i<=K:
            K=K-i
            s+='1'
        else:
            s+='0'
    print(s)


# Too many items
for _ in range(int(input())):
    N=int(input())
    count=0
    for i in range(1,N+1,10):
        count+=1
    print(count)

# Chef Fantasy 11
for _ in range(int(input())):
    N=int(input())
    if N==2:
        print(2)
    else:
        print(N*(N-1))
    

# Building Race
for _ in range(int(input())):
    A,B,X,Y=map(int,input().split())
    time_chef = A / X
    time_chefina = B / Y
    
    if time_chef < time_chefina:
        print("Chef")
    elif time_chef > time_chefina:
        print("Chefina")
    else:
        print("Both")


# Chef and Races
for _ in range(int(input())):
    A,B,X,Y=map(int,input().split())
    chef=[]
    arch=[]
    count=0
    chef.append(A)
    chef.append(B)
    arch.append(X)
    arch.append(Y)
    for i in chef:
        if i not in arch:
            count+=1
    print(count)
            
    