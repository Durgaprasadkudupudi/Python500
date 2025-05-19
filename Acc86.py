def binary(num):
    low=0
    high=num
    
    while(low<=high):
        mid=(low+high)//2
        if mid*mid==num:
            return mid
        if mid*mid>num:
            high=mid-1
        else:
            ans=mid
            low=mid+1
    return high

num=28
a=binary(num)
print(a)

def binary_root(num, n):
    low = 0
    high = num
    ans = -1
    
    while low <= high:
        mid = (low + high) // 2
        power = mid ** n
        
        if power == num:
            return mid
        elif power < num:
            ans = mid  # store potential answer
            low = mid + 1
        else:
            high = mid - 1
    return ans  # closest integer less than or equal to actual root

# Example
num = 69
n = 4
print(binary_root(num, n))  # Output: 2 (since 2^4 = 16 < 69, and 3^4 = 81 > 69)


import math

def binary(arr, t):
    def sumEle(arr, mid):
        total = 0
        for i in arr:
            total += math.ceil(i / mid)
        return total

    low = 1
    high = max(arr)
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        if sumEle(arr, mid) <= t:
            ans = mid       # possible answer, try to find smaller
            high = mid - 1
        else:
            low = mid + 1   # need a larger divisor
    return ans

arr = [1, 2, 3, 4, 5, 6]
t = 4
a = binary(arr, t)
print(a)

    