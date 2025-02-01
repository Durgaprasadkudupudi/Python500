# Easy Pronunciation
vowels='aeiou'
for i in range(int(input())):
    count=0
    N=int(input())
    S=input()
    easy=True
    for j in S:
        if j  in vowels:
            count=0
        else:
            count+=1
        if count>=4:
            easy=False
            break
    print("YES" if easy else "NO")

# cook your dish here
#TCS Examination
for _  in range(int(input())):
    dd,dt,dm=map(int,input().split())
    sd,st,sm=map(int,input().split())
    ssum=sd+st+sm
    dsum=dd+dm+dt
    if ssum>dsum:
        print("SLOTH")
    elif dsum>ssum:
        print("DRAGON")
    else:
        if dd>sd:
            print("DRAGON")
        elif sd>dd:
            print("SLOTH")
        else:
            if st>dt:
                print("SLOTH")
            elif dt>st:
                print("DRAGON")
            else:
                print("TIE")

for _ in range(int(input())):
    N = int(input())
    list1 = list(map(int, input().split()))
    
    # Count occurrences of each number
    frequency = {}
    for number in list1:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1
    
    # Check if any number occurs more than twice
    valid = True
    for count in frequency.values():
        if count > 2:
            valid = False
            break
    
    if valid:
        print("Yes")
    else:
        print("No")
                
# 1984 Leet code Bruit force Method             
class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        ans=float("inf")
        n=len(nums)
        for i in range(n):
            for j in range(i,n):
                temp=[]
                for m in range(i,j+1):
                    temp.append(nums[m])
                if len(temp)==k:
                    last=temp[-1]
                    first=temp[0]
                    ans=min(ans,last-first)
        return ans
    
# slinding Window approch
class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        ans=float("inf")
        n=len(nums)
        l=0
        for r in range(n):
            if(r-l== k ):
                l+=1
            if(r-l+1== k ):
                ans=min(ans,nums[r]-nums[l])
        return ans
        
    
            
    
    
    
    

