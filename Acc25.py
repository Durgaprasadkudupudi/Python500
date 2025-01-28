for _ in range(int(input())):
    N, X, K = map(int, input().split())
    # Calculate the number of bottles that can be filled
    bottles = min(N, K // X)
    print(bottles)

    # bath in Winters
for _ in range(int(input())):
    X, Y = map(int, input().split())
    
    buckets=X//Y
    persons=0
    for i in range(1,buckets,2):
        persons+=1
    print(persons)

    

# cook your dish here
for _ in range(int(input())):
    A,B=map(int,input().split())
    if A>B:
        print(">")
    elif B>A:
        print("<")
    else:
        print("=")


# cook your dish here
for _ in range(int(input())):
    N,K=map(int,input().split())
    lst=list(map(int,input().split()))
    lst2=[]
    count=0
    for i in lst:
        lst2.append(i+K)
    for j in lst2:
        if j%7==0:
            count+=1
    print(count)
            
        
        
    