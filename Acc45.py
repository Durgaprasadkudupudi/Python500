def binary(arr,target,n):
    low=0
    high=n-1
    ans=n
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]>=target):
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
arr=[1,2,3,4,5,5,6,8]
target=8
n=len(arr)
print("element is found at index : ",binary(arr,target,n))

# Get the number of triples
num_triples = int(input())

for _ in range(num_triples):
    # Read the three integers and create a sorted list
    numbers = sorted(map(int, input().split()))
    # Print the second maximum (middle element)
    print(numbers[1])



# cook your dish here
for _ in range(int(input())):
    X,Y=map(int,input().split())
    if Y>X:
        print("PROFIT")
    elif Y<X:
        print("loss")
    else:
        print("NEUTRAL")


def binarylower(arr,target,n):
    low=0
    high=n-1
    ans=n
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]>=target):
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
def binaryupper(arr,target,n):
    low=0
    high=n-1
    ans=n
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]>target):
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans

arr=[1,2,3,4,5,5,6,8]
target=8
n=len(arr)
lb=binarylower(arr,target,n)
if lb==n or arr[lb]!=target:
    print(-1) 
else:
    print("element found at index : ",lb,binaryupper(arr,target,n)-1)


for _ in range(int(input())):
    x=int(input())
    total=4*x
    if total>1000:
        print("NO")
    else:
        print("yes")