# you are given an array and you should find the maximum 
# length of the subarray which has atmost k ones

# example:
# [0,1,3,1,1,6,7,1,0,1]

arr=[0,1,3,1,1,6,7,1,0,1]
k=2
l=0
temp=0
ans=0
n=len(arr)

for r in range(n):
    if arr[r]==1:
        temp+=1
    while(temp>k):
        if arr[l]==1:
            temp-=1
        l+=1
    ans=max(ans,r-l+1)
print(ans)



# cook your dish here
for _ in range(int(input())):
    A, B = map(int, input().split())
    
    limak_candies = 0
    bob_candies = 0
    turn = 1
    
    while True:
        if turn % 2 == 1:  # Limak's turn
            if limak_candies + turn > A:
                print("Bob")
                break
            limak_candies += turn
        else:  # Bob's turn
            if bob_candies + turn > B:
                print("Limak")
                break
            bob_candies += turn
        
        turn += 1

# cook your dish here
# cook your dish here
for _ in range(int(input())):
    A,B,C = map(int, input().split())
    if A>50 and B<=50 and C<=50:
        print("A")
    if B>50 and A<=50 and C<=50:
        print("B")
    if C>50 and A<=50 and B<=50:
        print("C")
    if A<=50 and B<=50 and C<=50:
        print("NOTA")
    
    
class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        l=0
        ans=0
        temp=0
        for r in range(n):
            if(nums[r]==0):
                temp+=1
            while temp>k:
                if nums[l]==0:
                    temp-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans