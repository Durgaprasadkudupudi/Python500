class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        ans=0
        l=0
        uniset=set()
        for r in range(n):
            ch=s[r]
            if ch not in uniset:
                uniset.add(ch)
            else:
                while ch  in uniset:
                    uniset.remove(s[l])
                    l+=1
                uniset.add(ch)
            ans=max(ans,r-l+1)
        return ans