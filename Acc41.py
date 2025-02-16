def binary(arr,low,high,target):
   
    if low>high:
        return -1
    mid=(low+high)//2
    if arr[mid]==target:
        return mid
    elif target>arr[mid]:
        return binary(arr,mid+1,high,target)
    return binary(arr,low,mid-1,target)
arr=[1,2,4,5,6]
target=5
low=0
high=len(arr)-1
result=binary(arr,low,high,target)
print(result)