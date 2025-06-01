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
            high=mid-1
        if arr[mid]<=arr[high]:
            ans=min(ans,arr[mid])
            high=mid-1
        else:
            low=mid+1
    return ans
arr=[4,5,6,7,0,1,2]
n=len(arr)
print(binary(arr,n))


