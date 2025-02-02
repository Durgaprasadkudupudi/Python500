for _ in range(int(input())):
    N, K = map(int, input().split())
    protein_supply = list(map(int, input().split()))
    
    storage = 0
    possible = True
    
    for day in range(N):
        storage += protein_supply[day]
        
        if storage < K:
            print("NO", day + 1)
            possible = False
            break
        
        storage -= K
    
    if possible:
        print("YES")

for _ in range(int(input())):
    N,X=map(int,input().split())
    if N%2==0 or (N%2!=0 and X%2!=0):
        print("YES")
    else:
        print("No")


# 561 Leetcode
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=0
        nums.sort()
        for i in range(0,len(nums),2):
            ans+=nums[i]
        return ans
# 1343 Leetcode
class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """

        n=len(arr)
        ans=0
        temp=0
        l=0
        avg=0
        for r in range(n):
            temp+=arr[r]
            if r-l==k:
                temp-=arr[l]
                l+=1
            if r-l+1==k:
                if temp/k>=threshold:
                    ans+=1
        return ans
    


nums=[1,4,3,2]
k=10
l=0
ans=0
temp=0
n=len(nums)
for r in range(n):
    temp+=nums[r]

    while(temp>k):
        temp-=nums[l]
        l+=1
    ans=max(ans,r-l+1)
print(ans)
                
        