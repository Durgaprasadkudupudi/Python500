# # cook your dish here
x,y=map(int,input().split())
print(x-y)


# # cook your dish here
for _ in range(int(input())):
    x,n=map(int,input().split())
    marks=x/10
    res=marks*n
    print(int(res))


# # cook your dish here
X=int(input())
if X==404:
    print("Not found")
else:
    print("found")


# anagram

def anagram(dici1,dici2):
    if len(dici1)!=len(dici2):
        return False
    for i in dici1:
        if i not in dici2 or dici1[i]!=dici2[i]:
            return False
    return True

dici1={}
dici2={}
s1='litsen'
s2='silent'
for i in s1:
    if i in dici1:
        dici1[i]+=1
    else:
        dici1[i]=1
for j in s2:
    if j in dici2:
        dici2[j]+=1
    else:
        dici2[j]=1
ans=anagram(dici1,dici2)
print(ans)
