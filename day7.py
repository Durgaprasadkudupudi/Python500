#Sorting elements of an Array by Frequency in Python

a=[12,12,45,32,56,78,3,22,11]
a.sort()
print(a)


#finding the largest palindrome in a list 
a = ['prasad', 'madam', '123123', 'nana']
longest = ""

for ele in a:
    if ele == ele[::-1]:  # Check if the word is a palindrome
        if len(ele) > len(longest):  # Compare lengths to find the longest
            longest = ele

print(longest if longest else "No palindrome found")


# Python Program for Counting Distinct Elements in an Array

a=[12,23,12,12,45,56]
a=list(set(a))
print(a)

# Finding Repeating elements in an Array in Python

a=[12,4,21,44,4,21,12,34]


for i in a:
    if a.count(i)>1:
        print(i)

#Find non-repeating elements in an array Python

a=[12,21,44,4,21,12,34]

for i in a:
    if a.count(i)==1:
        print(i)