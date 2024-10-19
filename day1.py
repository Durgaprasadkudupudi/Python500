# Python Program to Find the Sum of First N Natural Numbers
# add function in Python Find the Sum of The First N Natural Numbers in Python Given an integer input the objective is to write a code to Find the Sum of First N Natural Numbers in C++. To do so we simply keep adding the value of the iter variable using a for loop.

#  Example

# Input : num = 8
# Output : 36

# Where first 8 number is 1, 2, 3, 4, 5, 6, 7, 8
# Sum of numbers = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = 36

num=5
sum=0
for i in range(num+1):
  sum=sum+i
print(sum)


#Python Program to Check Whether a Number is Even or Odd
# Check Whether a Number is Even or Odd in Python
# Check Whether a Number is Even or Odd in Python
#  Given an integer input num, the objective is to write a code to Check Whether a Number is Even or Odd in Python. To do so we check if the number is divisible by 2 or not, it’s Even if it’s divisible otherwise Odd.

# Example 
# Input : num = 3
#  Output : Odd 

num=int(input("enter the number :"))
if num%2==0:
  print("even")
else:
  print("odd")

# Find the Greatest of the Two Numbers
# Given two integer inputs as number1 and number2, the objective is to find the largest among the two. Therefore we’ll write a code to Find the Greatest of the Two Numbers in Python Language.

# Example
# Input : 20 40
# Output : 40

num1=int(input("enter the number :"))
num2=int(input("enter the number :"))
if num1>num2:
  print(num1)
else:
  print(num2)


# Find the Greatest of the Three Numbers
# Given three integer inputs the objective is to find the largest among them. Therefore we write a code to Find the Greatest of the Three Numbers in Python.

# Example
# Input : 20 30 10
# Output : 30

num1=int(input("enter the number :"))
num2=int(input("enter the number :"))
num3=int(input("enter the number :"))

if num1>num2 and num1>num3:
  print(num1)
elif num2>num1 and num2>num3:
  print(num2)
else:
  print(num3)

# Check if a Year is a Leap Year or Not in Python
# Given an integer input year, the objective of the code is to Check if a Year is a Leap Year or Not in Python Language. To do so  we’ll check if the year input satisfies either of the two conditions of leap year.

# Example
# Input : 2020
# Output : It's a Leap Year.

year=int(input("enter the year: "))

if year%400==0 or year%4==0 and year%100!=0:
  print("leap year")
else:
  print("not a leap year")