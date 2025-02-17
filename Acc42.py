N=int(input())
amt=N*2000
count=0
for i in range(1,amt+1,500):
    count+=1
print(count)

# cook your dish here
for _ in range(int(input())):
    X,H=map(int,input().split())
    if X>=H:
        print("YES")
    else:
        print("NO")

# cook your dish here
for _ in range(int(input())):
    N=int(input())
    if N%3==0:
        print("YES")
    else:
        print("NO")
