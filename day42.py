# cook your dish here
for _ in range (int(input())):
    a,x,b,y=map(int,input().split())
    sa=a*y 
    sb=b*x 
    if sa>sb:
        print("Alice")
    elif sb>sa:
        print("Bob")
    else:
        print("Equal")