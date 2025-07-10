import math
nums=[3,6,7,11]
h=8

def func(arr,hour):
    req=0
    for i in arr:
        req+=math.ceil(i/hour)
    return req


def binary(arr,h):
    ans=float('inf')
    low=1
    high=max(arr)
    while(low<=high):
        mid=(low+high)//2
        
        if (func(arr,mid))<=h:
            ans=min(ans,mid)
        if func(arr,mid)>h:
            low=mid+1
        else:
            high=mid-1
    return ans
print(binary(nums,h))