#shoes
for _ in range(int(input())):
    N, M = map(int, input().split())
    if M >= N:
        print(N)  
    else:
        print(N + (N - M))  


#factorial
# cook your dish here
for i in range(int(input())):
    n=int(input())
    fact=1
    if n==0 or n==1:
        print("1")
    elif n>1:
        for j in range(1,n+1):
            fact=fact*j
        print(fact)
    
# Mario and Transformation
T = int(input())
for _ in range(T):
    X = int(input())

    state = X % 3
    if state == 0:
        print("NORMAL")
    elif state == 1:
        print("HUGE")
    else:
        print("SMALL")