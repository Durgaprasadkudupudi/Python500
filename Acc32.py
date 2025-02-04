#2024 Maximize the Confusion of an Exam
class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        cnt1=0
        cnt2=0
        l=0
        ans=0
        n=len(answerKey)
        for r in range(n):
            if answerKey[r]=='T':
                cnt1+=1
            else:
                cnt2+=1
            while(min(cnt1,cnt2)>k):
                if answerKey[l]=='T':
                    cnt1-=1
                else:
                    cnt2-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans
    






nums=[1,1,0,0,1]
n=len(nums)
temp1=0
temp2=0
k=2
l=0
ans=0
for r in range(n):
    if nums[r]==0:
        temp1+=1
    else:
        temp2+=1
    while (min(temp1,temp2)>k):
        if nums[l]==0:
            temp1-=1
        else:
            temp2-=1
        l+=1
    ans=max(ans,r-l+1)
 
print(ans)

    
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
       
        if x >= 0:
            rev = int(str(x)[::-1])
        else:
            rev = -int(str(abs(x))[::-1])
        
       
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        
        return rev


for _ in range(int(input())):
    N = int(input())
    countOdd = (N + 1) // 2
    countEven = N // 2
    print(2 * countOdd * countEven)


for _ in range(int(input())):
    x, y, z = map(int, input().split())
    if x >= y:
        print("PIZZA")
    elif x >= z:
        print("BURGER")
    else:
        print("NOTHING")
        