# cook your dish here
for _ in range(int(input())):
    N,M=map(int,input().split())
    if M>N:
        print(0)
    else:
        print(N-M)


# cook your dish here
for _ in range(int(input())):
    X=int(input())
    if 67<=X<=45000:
        print("YES")
    else:
        print("NO")

# cook your dish here
for _ in range(int(input())):
    X=int(input())
    if X<30:
        print("NO")
    else:
        print("YES")


# cook your dish here
N=int(input())
if 6<=N<=8:
    print("YES")
else:
    print("NO")

# cook your dish here
# cook your dish here
N,M=map(int,input().split())
X,Y=map(int,input().split())
res1=N*X
res2=M*Y
res=res1+res2
print(res)
