from typing import *

def searchInARotatedSortedArrayII(A : List[int], key : int) -> bool:
   n=len(A)
   low=0
   high=n-1
   while(low<=high):
        mid=(low+high)//2
        if A[mid]==key:
           return True
        if A[low]==A[mid] and A[mid]==A[high]:
            low+=1
            high-=1
            continue
        #left sorted
        if A[low]<=A[mid]:
            if A[low]<=key<=A[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            if A[mid]<=key<=A[high]:
                low=mid+1
            else:
                high=mid-1
