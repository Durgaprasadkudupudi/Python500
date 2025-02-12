# cook your dish here
A,B=map(int,input().split())
pres=A+B
res=str(pres)+"1"
print(int(res))

for _ in range(int(input())):
    N,X=map(int,input().split())
    print(N-X)


# cook your dish here
for _ in range(int(input())):
    X,Y=map(int,input().split())
    print(abs(X-Y))