a=10
b=30
count=0
for i in range(a,b+1):
    if i%2==0:
        count+=1
        if count==1:
            continue
        if count%2!=0 :
            print(i)
    #10- 20 , 14,16,20,24,28
def binary(arr,n):
    low=0
    high=n-1
    ans=float('inf')
    while(low<=high):
        mid=(low+high)//2
        if arr[low]<=arr[mid]:
            ans=min(ans,arr[low])
            low=mid+1
        else:
            ans=min(arr[mid],ans)
            high=mid-1
    return ans
arr=[4,5,6,0,1,2]
n=len(arr)
print(binary(arr,n))