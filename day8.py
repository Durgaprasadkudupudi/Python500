# #Problem Description :
# The function accepts two positive integers ‘r’ and ‘unit’ and a positive integer array ‘arr’ of size ‘n’ as its argument ‘r’ represents the number of rats present in an area, ‘unit’ is the amount of food each rat consumes and each ith element of array ‘arr’ represents the amount of food present in ‘i+1’ house number, where 0 <= i

# Note:

# Return -1 if the array is null
# Return 0 if the total amount of food from all houses is not sufficient for all the rats.
# Computed values lie within the integer range.
# Example:

# Input:

# r: 7
# unit: 2
# n: 8
# arr: 2 8 3 5 7 4 1 2
# Output:

# 4

# Explanation:
# Total amount of food required for all rats = r * unit

# = 7 * 2 = 14.

def calcfood(arr,unit,r):
    if len(arr)==0:
        return -1
    total_food=r*unit
    food_consumed=0
    for i in arr:
        food_consumed+=i
        if food_consumed>=total_food:
            return 0
        
arr=[1,2,3,5,6]
print(calcfood(arr,2,7)) 


#sorting the array in accending order without using inbuilt functions

arr1=[23,2,45,32,12,3]
n=len(arr1)
for i in range(n):
    for j in range(i+1, n): 
        if arr1[i]>arr1[j] :
            arr1[i], arr1[j] = arr1[j], arr1[i]
print(arr1)



#sorting the array in decending order without using inbuilt functions

arr1=[23,2,45,32,12,3]
n=len(arr1)
for i in range(n):
    for j in range(i+1, n): 
        if arr1[i]<arr1[j] :
            arr1[i], arr1[j] = arr1[j], arr1[i]
print(arr1)

#finding the minimum scalor product

arr1=[23,2,45,32,12,3]
n=len(arr1)
for i in range(n):
    for j in range(i+1, n): 
        if arr1[i]>arr1[j] :
            arr1[i], arr1[j] = arr1[j], arr1[i]
print(arr1)

arr2=[23,2,45,32,12,3]
n=len(arr2)
for i in range(n):
    for j in range(i+1, n): 
        if arr2[i]<arr2[j] :
            arr2[i], arr2[j] = arr2[j], arr2[i]
print(arr2)

product = 0
for i in range(n):
    product += arr1[i]*arr2[i]

print(product)

#finding the maximum scalor product in a arrays
arr1 = [1, 2, 6, 3, 7]
arr2 = [10, 7, 45, 3, 7]
n = len(arr1)

#Sort arr1 in ascending order
arr1.sort()

#Sort arr2 in descending order
arr2.sort()

product = 0
for i in range(n):
    product += arr1[i]*arr2[i]

print(product)