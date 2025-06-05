a='abcbbab'
b='abcbbab'

dic1={}
dic2={}

for i in a:
    if i in dic1:
        dic1[i]+=1
    else:
        dic1[i]=1
for j in b:
    if j in dic2:
        dic2[j]+=1
    else:
        dic2[j]=1
print(dic1)
print(dic2)

if dic1==dic2:
    print("anagram")
else:
    print("Not an Anagram")


def func(dic1,dic2):
    if len(dic1)!=len(dic2):
        return False
    for key in dic1:
        if key not in dic2 or dic1[key] != dic2[key]:
            return False
    return True
s = "cbaebabacd"
p='abc'
l=0
ans=[]
temp=''
dic1={}
dic2={}
k=len(p)
n=len(s)
#frequency count for p
for i in p:
    if i in dic1:
        dic1[i]+=1
    else:
        dic1[i]=1
for r in range(n):
    temp=s[r]
    
    for i in temp:
        if i in dic2:
            dic2[i]+=1
        else:
            dic2[i]=1
    if r-l==k:
        lval=s[l]
        dic2[lval]-=1
        if dic2[lval]==0:
            dic2.pop(lval)
        l+=1
        
    if r-l+1==k:
        if func(dic1,dic2):
            ans.append(l)
print(ans)
        




