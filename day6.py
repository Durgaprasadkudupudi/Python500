# Sum of Elements in an array using Python

a=[1,2,3,5]
sum=0
for i in a:
    sum=sum+i
print(sum)

# Reverse an Array using Python

a=[1,2,3,5]

b=a[::-1]

print("reversed array :",b)


# Python program to Sort first half in ascending order and second half in descending order in an array

a=[23,45,222,2,45,232,13,34]

a.sort()

n=len(a)

print(n//2)

for i in range(n//2):
    print(a[i])
for j in range(n - 1, n // 2 -1, -1) :
        print(a[j], end = " ")


# Python Program to sort the elements of an array

a=[23,45,222,2,45,232,13,34]

a.sort()

print("accending order",a)
b=[23,45,222,2,45,232,13,34]

b.sort(reverse=True)

print("descending order",b)



# Frequency of Elements in an Array in Python
# Here, in this page we will discuss the program to count the frequency of elements in an array in python programming language. We are given with an array
# and need to print each element along its frequency.

b=[23,45,222,2,45,232,13,34]

for i in b:
     ele=i
     count=b.count(i)
     print(f"{ele} is {count} times")
