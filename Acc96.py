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
        