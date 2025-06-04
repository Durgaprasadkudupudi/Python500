arr=[1,1,1,0,0,0,1,1,1,1,0]
l=0
cnt1=0
cnt2=0
ans=0
k=2
n=len(arr)
for r in range(n):
    if arr[r]==0:
        cnt1+=1
    else:
        cnt2+=1
    while(min(cnt1,cnt2)>k):
        if arr[l]==0:
            cnt1-=1
        else:
            cnt2-=1
        l+=1
    ans=max(ans,r-l+1)
    
    print(arr[l:r+1])
print(ans)


s=[1,2,3,2,2]
l=0
n=len(s)
ans=0
k=2
dic={}
for r in range(n):
    if s[r] in dic:
        dic[s[r]]+=1
    else:
        dic[s[r]]=1
    while(len(dic)>k):
        dic[s[l]]-=1
        if dic[s[l]]==0:
            dic.pop(s[l])
        l+=1
    ans=max(ans,r-l+1)
print(ans)