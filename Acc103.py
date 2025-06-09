class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        def atMost(k):
            if k < 0:
                return 0
            res = 0
            left = 0
            curr_sum = 0
            for right in range(len(nums)):
                curr_sum += nums[right]
                while curr_sum > k:
                    curr_sum -= nums[left]
                    left += 1
                res += right - left + 1
            return res

        return atMost(goal) - atMost(goal - 1)
