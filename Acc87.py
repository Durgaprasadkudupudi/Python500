import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        
        def total(piles, mid):
            t = 0
            for pile in piles:
                t += math.ceil(pile / float(mid))
            return t

       
        def binarySearch(piles, h):
            low = 1
            high = max(piles)
            
            while low <= high:
                mid = (low + high) // 2
                total_time = total(piles, mid)
                
                if total_time <= h:
                    high = mid - 1  
                else:
                    low = mid + 1 

            return low 

        return binarySearch(piles, h)
