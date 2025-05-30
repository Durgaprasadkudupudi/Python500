class Solution(object):
    def countGoodSubstrings(self, s):
        ans=0
        n=len(s)
        k=3
        l=0
        dic={}
        for r in range(n):
            if s[r] in dic:
                dic[s[r]]+=1
            else:
                dic[s[r]]=1

            if r-l==k:
                dic[s[l]]-=1
                if dic[s[l]]==0:
                    dic.pop(s[l])
                l+=1
            if len(dic)==k:
                ans+=1
        return ans