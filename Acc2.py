# You are given a function,
# int findCount(int arr[], int length, int num, int diff);

# The function accepts an integer array ‘arr’, its length and two integer variables ‘num’ and ‘diff’. 
# Implement this function to find and return the number of elements of ‘arr’ having an absolute difference of less than or equal to ‘diff’ with ‘num’.
# Note: In case there is no element in ‘arr’ whose absolute difference with ‘num’ is less than or equal to ‘diff’, return -1.

# Example:
# Input:

# arr: 12 3 14 56 77 13
# num: 13
# diff: 2
# Output:
# 3

# Explanation:
# Elements of ‘arr’ having absolute difference of less than or equal to ‘diff’ i.e. 2 with ‘num’ i.e. 13 are 12, 13 and 14.

# */

def calculate(num,diff,arr):
    count = 0
    for i in arr:
        difference=num-i
        if(abs(difference)<=diff):
            count+=1
    print(count)

num=13
diff=2
arr=[12,3,14,56,77,13]
calculate(num,diff,arr)


#perfect square

num=16
for i in range(1,num+1):
    if i**2==num:
        print("yes")
        break
else:
    print("no")


#sum of the digits in a string

n=input("enter a string:")
sum=0
lst='1234567890'
for i in n:
    if i in lst:
        sum+=int(i)
print(sum)