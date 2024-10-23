# A Harshad number is a positive integer that is divisible by the sum of the digits of the integer. It is also called the Niven number.

# For Example : 153
# Sum of digits = 1 + 5 + 3 = 9

# 153is divisible by 9 so 153 is a Harshad Number.

n=int(input("enter a number:"))

sum_digits=0

m=str(n)

for i in m:
    sum_digits+=int(i)
if n%sum_digits==0:
    print("Harshed Number")
else:
    print("Not a Harshed Number")


# Largest Element in an array using python
# Here, in this page we will discuss the program 
# to find the largest element in an array using python we are given with an array elements and we need to print the largest among the given elements. We discuss different methods to find the largest element using python programing language.

list1=[1,23,45,32,43,67,2,322]

largest=list1[0]

for i in list1:
    if i>largest:
        largest=i
print(largest)



# Find smallest element in an array using Python

# In this section we will learn how to find smallest element in an array using python programming language which is the scripting language. 
# If we want to find smallest element from the array enter by the user so we have to compare one element to other until we get the desired element and print it.


list2=[34,34,21,13,11,34,4]
min_ele=list2[0]

for i in list2:
    if i<min_ele:
        min_ele=i
print(min_ele)

# Find Second Smallest Element in an Array using Python

list2=[34,34,21,13,11,34,4]

list3=list2.sort()
print(list2[1])


#sum of the digits in a array

list2=[34,34,21,13,11,34,4]

sum_digits=0

for i in list2:
    sum_digits+=i
print("sum of the elements in a list:",sum_digits)

