arr=[2,2,2,2,5,5,5,8]
l=0
n=len(arr)
temp=[]
k=3
avg=0
ans=0
t=4
for r in range(n):
    temp.append(arr[r])
    
    if r-l==k:
        temp.pop(0)
        l+=1
    if r-l+1==k:
        avg=sum(temp)/len(temp)
        if avg>=t:
            print(temp)
            print(avg)
            ans+=1
print(ans)
            
    
    
    
    
    