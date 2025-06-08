class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def CountExact(arr,k):
            l=0
            n=len(arr)
            temp=0
            ans=0
            for r in range(n):
                if arr[r]%2==1:
                    temp+=1
                while(temp>k):
                    if arr[l]%2==1:
                        temp-=1
                    l+=1
                ans+=r-l+1
            return ans
        return CountExact(nums,k)-CountExact(nums,k-1)
        