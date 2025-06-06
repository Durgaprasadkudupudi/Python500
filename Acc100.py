class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        temp = 0
        n = len(nums)
        ans = float('inf')

        for r in range(n):
            temp += nums[r]

            while temp >= target:
                ans = min(ans, r - l + 1)
                temp -= nums[l]
                l += 1

        return ans if ans != float('inf') else 0
