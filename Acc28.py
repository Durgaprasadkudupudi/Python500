# Sliding Window Approch
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2=[]
n=len(list1)
l=0
temp=0
k=3
for r in range(n):
    temp+=list1[r]

    if r-l==k:
        temp-=list1[l]
        l+=1
    if r-l+1==k:
        list2.append(temp)

list2.sort()
print(list2[-1])

#Substring of size 3 with distinct characters(1876)
class Solution(object):
    def countGoodSubstrings(self, s):
        n=len(s)
        lst=[]
        ans=0
        for i in range(n):
            for j in range(i,n):
                temp=[]
                for k in range(i,j+1):
                    temp.append(s[k])
                if len(temp)==3 and len(set(temp))==3:
                    ans+=1
        return ans
    

s='xyzzaz'
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
print(ans)


for _ in range(int(input())):
    n = int(input())  # Read the number of terms
    coefficients = list(map(int, input().split()))  # Read the coefficients

    # Find the degree of the polynomial by looking for the last non-zero coefficient
    degree = n - 1  # Start from the last index
    while coefficients[degree] == 0:  # Move backwards until a non-zero is found
        degree -= 1
        
    print(degree)

# Recent contest problems
for _ in range(int(input())):
    n=int(input())
    l=list(map(str,input().split()))
    s="START38"
    lt='LTIME108'
    a=l.count(s)
    b=l.count(lt)
    print(a,b)

def is_prime(n):
    if n < 2:
        return "no"
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return "no"
    return "yes"

# Number of test cases
for _ in range(int(input())):
    n = int(input())
    print(is_prime(n))


        

