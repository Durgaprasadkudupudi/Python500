nums=[7,7,7,7,13,11,12,7]
m=2
k=3

def func(arr, mid, k):
    count = 0   # count of current streak of valid (>= mid)
    b = 0  # how many valid groups formed

    for i in arr:
        if i <= mid:
            count += 1
            if count == k:
                b += 1
                count = 0  # reset to avoid overlapping
        else:
            count = 0  # break streak if element < mid
    return b
    
print(func(nums,12,k))

def binary(arr,m,k):
    ans=float('inf')
    low=1
    high=max(arr)
    while(low<=high):
        mid=(low+high)//2
        
        if func(arr,mid,k)==m:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return low
print(binary(nums,m,k))
            

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