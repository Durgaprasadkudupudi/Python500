for _ in range(int(input())):
    w,x,y,z=map(int,input().split())
    final=w+y*z
   
    if final==x:
        print("filled")
    elif final>x:
        print("overflow")
    else:
        print("unfilled")

def Finddays(weights,cap):
    days=1
    load=0
    n=len(weights)
    for i in range(n):
        if load+weights[i]>cap:
            days+=1
            load=weights[i]
        else:
            load+=weights[i]
    return days
        
def leastweight(weights,d):
    low=max(weights)
    high=sum(weights)
    while(low<=high):
        mid=(low+high)//2
        NumberofDays=Finddays(weights,mid)
        if NumberofDays<=d:
            high=mid-1
        else:
            low=mid+1
    return low
weights=[1,2,3,4,5,6,7,8,9,10]
days=5
ans=leastweight(weights,days)
print(ans)