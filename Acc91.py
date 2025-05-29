li=[1,2,3,4]
n=len(li)
ans=0
for i in range(n):
    for j in range(i,n):
        temp=[]
        tsum=0
        for k in range(i,j+1):
            temp.append(li[k])
            tsum+=li[k]
        if len(temp)==3:
            print(temp)
            ans=max(ans,tsum)
            
print(ans)

        