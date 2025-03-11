# cook your dish here
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    reqtime=x*y
    total=z*24*60
    if total>=reqtime:
        print("yes")
    else:
        print("NO")

# cook your dish here

a,b,c,d=map(int,input().split())
list2=[]
list2.append(a)
list2.append(b)
list2.append(c)
list2.append(d)
count=0
for i in list2:
    if i>=10:
        count+=1
print(count)


# cook your dish here
for _ in range(int(input())):
    n,m,k=map(int,input().split())
    space=m-k
    if n <=space:
        print("YES")
    else:
        print("NO")
    