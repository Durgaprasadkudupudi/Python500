for _ in range(int(input())):
    x,y=map(int,input().split())
    xrupees=x*100
    yrupees=y*10
    if xrupees>=yrupees:
        print("CLOTH")
    else:
        print("DISPOSABLE")

# cook your dish here
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    if x>y and x>z:
        print("Setter")
    elif y>x and y>z:
        print("Tester")
    else:
        print("Editorialist")

for _ in range(int(input())):
    x=int(input())
    time=x*60
    print(time//30)

for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    aprice=a-c
    bprice=b-d
    if aprice>bprice:
        print("second")
    elif bprice>aprice:
        print("First")
    else:
        print("Any")