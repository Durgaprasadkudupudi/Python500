for _ in range(int(input())):
    x,y=map(int,input().split())
    total=x*3
    if y>=total:
        print("YES")
    else:
        print("NO")

for _ in range(int(input())):
    x,y=map(int,input().split())
    dr=x*3
    tr=y*2
    if dr>=tr:
        print(tr)
    else:
        print(dr)

for _ in range(int(input())):
    n,m,x=map(int,input().split())
    l=2*n
    w=2*m
    total=(l+w)*x
    print(total)

for _ in range(int(input())):
    x=int(input())
    if x<10:
        print(x)
    else:
        print(x%10)

n=int(input("enter a integer:"))
low=1
high=n
ans=n
while(low<=high):
    mid=(low+high)//2
    if mid*mid<=n:
        low=mid+1
        ans=mid
    else:
        high=mid-1
print(ans)

class Solution(object):
    def countGoodSubstrings(self, s):
        k=3
        n=len(s)
        ans=0
        l=0
        dici={}
        for r in range(n):
            if s[r] in dici:
                dici[s[r]]+=1
            else:
                dici[s[r]]=1
            if r-l==k:
                dici[s[l]]-=1
                if dici[s[l]]==0:
                    dici.pop(s[l])
                l+=1
            if len(dici)==k:
                ans+=1
        return ans
        