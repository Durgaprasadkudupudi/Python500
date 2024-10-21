# Find the Fibonacci Series up to Nth Term in Python
# Given an integer as an input, the objective is to find the Fibonacci series until the number input as the Nth term. Therefore, we write a program to Find the Fibonacci Series up to Nth Term in Python Language.

# Example
# Input : 4
# Output : 0 1 1 2

n=int(input("enter a number:"))
n1=0
n2=1
print(n1)
print(n2)
for  i in range(n+1):
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3

# Factorial of a Number in Python
# Here we will discuss how to find the Factorial of a Number in Python programming language.

# Factorial of any number is the product of it and all the positive numbers below it for example factorial of 5 is 120

# Factorial of n (n!) = 1 * 2 * 3 * 4....n
# 5! = 1 x 2 x 3 x 4 x 5 = 120 7! = 1 x 2 x 3 x 4 x 5 x 6 x 7 = 5040

n=int(input("enter a number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)

# Find the Power of a Number in Python Language
# Given two integer input numbers, the objective is to find the power of the number raise to the power variable. Therefore, we’ll write a code to Find the Power of a Number in Python Language.

# Example
# Input : 2 3
# Output : 8

n=int(input("enter a number:"))

power=int(input('enter a power:'))

digit= n**power

print(digit)

# Find the Factors of a Number in Python
# Given an integer Number as input, the objective is to search for all the factors of the Given integer input. Therefore, we write a program to Find the Factors of a Number in Python Language.

# Example
# Input : 10
# Output : 2 5

n=int(input("enter a number:"))
for i in range(1,n+1):
    if n%i==0:
        print(i,end=' ')

# Check Whether or Not the Number is a Perfect Number in Python
# Given an integer input as a number, the objective is to check whether or not a number is a Perfect Number in Python Language. Therefore, we write a program to Check Whether or Not the Number is a Perfect Number in Python Language.

# Example
# Input : 28
# Divisors : [1, 2, 4, 7, 14]
# Sum = 1 + 2 + 4 + 7 + 14 = 28
# Output : It's a Perfect Number

n=int(input("enter a number:"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if sum==n:
    print("it's a perfect number")
else:
    print("not a perfect number")