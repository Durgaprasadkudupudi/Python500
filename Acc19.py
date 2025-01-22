for i in range(int(input())):
    N,X=map(int,input().split())
    res=N/X
    if res%2==0:
        print("yes")
        
    else:
        print("No")



# cook your dish here
for i in range(int(input())):
    N=int(input())
    sqrt=N**0.5
    print(int(sqrt))


T=int(input())
for i in range (T):
    dd,dt,dm=map(int,input().split())
    sd,st,sm=map(int,input().split())
    if (dd+dt+dm)>(sd+st+sm):
        print("DRAGON")
    elif (dd+dt+dm)<(sd+st+sm):
        print("SLOTH")
    elif (dd+dt+dm)==(sd+st+sm):
        if dd>sd:
            print("DRAGON")
        elif dd<sd:
            print("SLOTH")
        elif dd==sd:
            if dt>st:
                print("DRAGON")
            elif dt<st:
                print("SLOTH")
            elif dt==st:
                print("TIE")