class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[n - 1] != nums[n - 2]:
            return nums[n - 1]
        
        low = 1
        high = n - 2
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            
            # Corrected placement of update conditions
            if (mid % 2 == 1 and nums[mid] == nums[mid - 1]) or (mid % 2 == 0 and nums[mid] == nums[mid + 1]):
                low = mid + 1  # Move to the right half
            else:
                high = mid - 1  # Move to the left half
        
        return -1  # Fallback, should never hit this in a valid input


# cook your dish here
for _ in range(int(input())):
    N,X,Y=map(int,input().split())
    total=X*Y
    if total>=N:
        print("YES")
    else:
        print("NO")

for _ in range(int(input())):
    G,B=map(int,input().split())
   
    print(B-G)

for _ in range(int(input())):
    # cook your dish here
    X=int(input())
    if X>98:
        print("YES")
    else:
        print("NO")    

for _ in range(int(input())):
    # cook your dish here
    X=int(input())
    if X>=7:
        print("NO")
    else:
        print("YES")    