import math

def calc(arr,d):
    sum=0
    for i in arr:
        sum+=math.ceil(i/d)
    return sum
def binary(arr,t):
    ans=-1
    low=1
    high=max(arr)
    while(low<=high):
        mid=(low+high)//2
        if calc(arr,mid)<=t:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
    
arr=[1,2,5,9]
h=6
print(binary(arr,h))
            