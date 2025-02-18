# cook your dish here
for _ in range(int(input())):
    X,Y=map(int,input().split())
    if X>=Y:
        print("YES")
    else:
        print("NO")

for _ in range(int(input())):
    N=int(input())
    if N%2==0:
        print("YES")
    else:
        print("NO")

# cook your dish here
for _ in range(int(input())):
    X,Y=map(int,input().split())
    top=10*X
    res=90*Y
    sum=top+res
    print(sum)

for _ in range(int(input())):
    X,Y=map(int,input().split())
   
    res=X*Y
    
    print(res)

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
       

        if needle in haystack:
            return haystack.find(needle)  
        else:
            return -1 