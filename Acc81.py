def binary(a,t):
    l=0
    h=len(a)-1
    while(l<=h):
        mid=(l+h)//2
        if a[mid]==t:
            return mid
        elif t>a[mid]:
            l=mid+1
        else:
            h=mid-1
    return -1
a=[1,2,4,5,7,9]
t=9
b=binary(a,t)
print(b)



def binary(l,h,arr,t):
    if l>h:
        return -1
    mid=(l+h)//2
    if arr[mid]==t:
        return mid
    elif arr[mid]>t:
        return binary(l,mid-1,arr,t)
    elif arr[mid]<t:
        return binary(mid+1,h,arr,t)
    return -1

arr=[23,56,57,89,90]
l=0
h=len(arr)-1
t=90
print(binary(l,h,arr,t))


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low=0
        high=len(nums)-1
        ans=len(nums)
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]>=target:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
        