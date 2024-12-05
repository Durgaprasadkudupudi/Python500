def canMakeEqualProducts(n, arr):
    # Find the product of all elements in the array
    total_product = 1
    for num in arr:
        total_product *= num

    # The target product for each element
    target = total_product ** (1 / n)

    # Check if target is an integer
    if target != int(target):
        return "No"

    target = int(target)

    # Check if each number can be multiplied by integers to reach the target
    for num in arr:
        if target % num != 0:
            return "No"

    return "Yes"

# Input
n = 3
arr = [50, 75, 100]

# Output
print(canMakeEqualProducts(n, arr))


arr=[50,75,100]
res=[]
for i in range(len(arr)):
  result=arr[i]*2
  if arr[i]*2==result:
    res.append(result)
  elif arr[i]*3==result:
    res.append(result)
  elif arr[i]*2*2==result:
    res.append(result)
print(res)


def maxSubarrayProduct(arr, n):

    # Initializing result
    result = arr[0]

    for i in range(n):

        mul = arr[i]

        # traversing in current subarray
        for j in range(i + 1, n):
            result = max(result, mul)
            mul *= arr[j]

        # updating the result for (n-1)th index.
        result = max(result, mul)

    return result

arr = [ 1, -2, -3, 0, 7, -8, -2 ]
n = len(arr)
print("Maximum sub-array product is" , maxSubarrayProduct(arr, n))

#Friendly pairs
def friendlypair(pairs):
  s=set()
  for (x,y) in pairs:
    s.add((x,y))
    if (y,x) in s:
        print(y,x)
pairs = [(3, 4), (1, 2), (5, 2), (7, 10), (4, 3), (2, 5)]
friendlypair(pairs)


a=[12,3,4,5,221,21,42]
count1=0
count2=0
for i in a:
  if i%2==0:
    count1=count1+1
  else:
    count2=count2+1
print(count1)
print(count2)