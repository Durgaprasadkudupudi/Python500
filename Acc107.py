from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(arr, n) :
    cur_sum=0
    max_sum=float('-inf')
    for i in arr:
        cur_sum+=i
        max_sum=max(cur_sum,max_sum)

        if cur_sum<0:
            cur_sum=0
    if max_sum>0:
        return max_sum
    else:
        return 0

#taking inpit using fast I/O
def takeInput() :
	
    n =  int(input())

    if(n == 0) :
        return list(), n

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


#main
arr, n = takeInput()
print(maxSubarraySum(arr, n))
