def rotated(arr,n,target):
    low=0
    high=n-1
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]==target:
            return True
        if arr[mid]==arr[low] and arr[mid]==arr[high]:
            low+=1
            high-=1
            
        if arr[low]<=arr[mid]:
            if arr[low]<=target<=arr[mid]:
                high=mid-1
            else:
                low=mid+1
        if arr[mid]<=arr[high]:
            if arr[mid]<=target<=arr[high]:
                low=mid+1
            else:
                high=mid-1
    return False
arr=[3,1,2,3,3,3,3,3]
target=3
n=len(arr)
print(rotated(arr,n,target))


def singe(arr,n):
    n=len(arr)
    if arr[0]!=arr[1]:
        return arr[0]
    if arr[n-1]!=arr[n-2]:
        return arr[n-1]
    if len(arr)==1:
        return arr[0]
    low=1
    high=n-2
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]!=arr[mid-1] and arr[mid]!=arr[mid+1]:
            return arr[mid]
        if ((mid % 2 == 1 and arr[mid] == arr[mid - 1]) or 
    (mid % 2 == 0 and arr[mid] == arr[mid + 1])):

            low=mid+1
        else:
            high=mid-1
    return -1
arr=[1,1,2,2,3,4,4,5,5]
n=len(arr)
a=singe(arr,n)
print(a)


def maximum(arr,n):
    if len(arr)==1:
        return arr[0]
    if arr[0]>arr[1]:
        return arr[0]
    if arr[n-1]>arr[n-2]:
        return arr[n-1]
    low=1
    high=n-2
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
            return arr[mid]
        if arr[mid]>arr[mid-1]:
            low=mid+1
        else:
            high=mid-1
    return -1
arr=[1,2,3,4,5,6,7,8,5,1]
n=len(arr)
a=maximum(arr,n)
print(a)