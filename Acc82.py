def first(arr,n,t):
    low=0
    high=len(arr)-1
    f=-1
    while(low<=high):
        mid=(high+low)//2
        if arr[mid]>=t:
            high=mid-1
            f=mid
        else:
            low=mid+1
    return f
    
def last(arr,n,t):
    low=0
    high=len(arr)-1
    l=-1
    while(low<=high):
        mid=(high+low)//2
        if arr[mid]>t:
            high=mid-1
            l=mid
        else:
            low=mid+1
    return l
arr = [5,7,7,8,8,10]
n=len(arr)
t=5
print(first(arr,n,t))
print(last(arr,n,t))
    

def binary(arr,n,t):
    low=0
    high=len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]==t:
            return mid
        if arr[low]<=arr[mid]:
            if arr[low]<=t<=arr[mid]:
                high=mid-1
            else:
                low=mid+1
        if arr[mid]<=arr[high]:
            if arr[mid]<=t<=arr[high]:
                low=mid+1
            else:
                high=mid-1
arr=[4,5,1,2,3]
n=len(arr)
t=3
print(binary(arr,n,t)) 