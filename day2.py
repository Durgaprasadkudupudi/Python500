# Find the sum of the Digits of a Number in Python
# Given an input the objective to find the Sum of Digits of a Number in Python. To do so we’ll first extract the last element of the number and then keep shortening the number itself.

# Example
# Input : number = 123
# Output : 6

num= input("enter a number:")
sum=0

for i in num:
    sum = sum + int(i)
print(sum)


# Find the Reverse of a Number in Python
# Given an integer input the objective is to reverse the given integer number using loops and slicing. Therefore, we’ll write a program to Find the Reverse of a Number in Python Language.

# Example
# Input : 123
# Output : 321

num=input("enter a number:")

rev_num = num[::-1]

print(rev_num)

# Check Whether or Not the Number is a Palindrome in Python
# Given an integer number as an input, the objective is to check Whether or not the number is a palindrome. Therefore, we write a code to Check Whether or Not the Number is a Palindrome in Python Language.

# Example
# Input : 1221
# Output : Palindrome

num=input("enter a number:")

rev_num = num[::-1]

if num==rev_num:
    print("palindrome")
else:
    print("not palindrome")

# Check Whether a Given Number is an Armstrong Number or Not in Python
# For a given integer the objective is to check whether or not the given integer is an Armstrong number or not. The Armstrong number is briefly defined in the section below.

# Example
# Input : 371
# Output : It's an Armstrong Number

num=input("enter number:")

sum=0

len_num=len(num)

for i in num:
    sum=sum+i**len_num
if sum==num:
    print("it's an armstrong number")
else:
    print("it's not an armstrong number")



# Find the Armstrong Number in a given Range in Python
# Given two integers high and low for limits as inputs, the objective is to write a code to Find the Armstrong Numbers in a given Interval in C++. 

# For Instance,
# Input : 150 160
# Output : 153

for i in range(150,160):
    sum=0
    len_num=len(str(i))
    for j in str(i):
        sum=sum+int(j)**len_num
    if sum==i:
        print(i,"is an armstrong number")
   
