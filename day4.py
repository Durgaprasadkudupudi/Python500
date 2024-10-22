#check whether the given number is perfect number or not

n=int(input("enter a number:"))
square_root=n**0.5

if(n==square_root*square_root):
    print("perfect number")
else:
    print("not a perfect number")

#strong Number

# Strong Numbers is a number in which the sum of the factorial of individual digits of the numbers is equal to the number itself.

# For Example: 145 
# 145 = 1! x 4! x 5! =  145

def fact(n):
  if n==0:
    return 1
  else:
    return n*fact(n-1)
m=int(input("enter a number:"))
y=str(m)
sum=0
for i in y:
  n=int(i)
  sum=sum+fact(n)
if sum==m:
    print("strong number")
else:
    print("not a strong number")

# An Automorphic number is a special number, whose’s square ends with the same digits as the number itself

n=5
m=n*n
y=str(n)
a=len(y)
z=y[::-1]
x=z[:a+1]
if int(x)==n:
  print("yes")
else:
  print("no")


#   Friendly Pair

# two numbers num1 & num2 are friendly pairs if the following holds true -

# (Sum of divisors of num1)/num1= (Sum of divisors of num2)/num2

num1=int(input("enter num1:"))
num2=int(input("enter num2"))
sum1=0
sum2=0
for i in range(1,num1+1):
   if num1%i==0:
      sum1=sum1+i
for j in range(1,num2+1):
   if num2%j==0:
      sum2+=j
if sum1/num2==sum2/num1:
   print("friendly pair")
else:
   print("not a friendly pair")



# Abundant number is an number in which the sum of the proper divisors of the number is greater than the number itself.

# Ex:- Abundant number 12 having a proper divisor is 1, 2, 3, 4, 6 

# The sum of these factors is 16 it is greater than 12 
# So it is an Abundant number

# Some other abundant numbers: 

# 18, 20, 30, 70, 78, 80, 84, 90, 96, 100, 104, 108, 120

n=int(input("enter a number:"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if sum>n:
    print("it's a abundant number")
else:
    print("not a abundant number")

