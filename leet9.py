# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
      
        def guessnumber(n):
            low=0
            high=n
            while(low<=high):
                mid=(low+high)//2
                result=guess(mid)
                if result==0:
                    return mid
                if result==-1:
                    high=mid-1
                else:
                    low=mid+1
        return guessnumber(n)
for _ in range(int(input())):
    c,x,y=map(int,input().split())
    if c==x:
        print(0)
    elif c>x:
        rem=(c-x)*y
        print(rem)
    elif x>c:
        print(0)

        