# count words

a="hello world how are you"

lst=a.split()
print(len(lst))

# find the GCD

a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
lst=[]
maximum=max(a,b)
for i in range(1,maximum+1):
    if a%i==0 and b%i==0:
        lst.append(i)
lst.sort(reverse=True)
print(lst[0])


#lucky 7

a="rtyrturuytiyit7ti"
b=a[6]
print(b)


#perfect number
a=int(input("Enter the number"))
sum=0
for i in range(1,a):
    if a%i==0:
        sum=sum+i
if sum==a:
    print("Perfect number")
else:
    print("Not a perfect number")

# Janmansh and Assignments
# Janmansh has to submit 
# 3
# 3 assignments for Chingari before 
# 10
# 10 pm and he starts to do the assignments at 
# X
# X pm. Each assignment takes him 
# 1
# 1 hour to complete. Can you tell whether he'll be able to complete all assignments on time or not?

# Input Format
# The first line will contain 
# T
# T - the number of test cases. Then the test cases follow.
# The first and only line of each test case contains one integer 
# X
# X - the time when Janmansh starts doing the assignments.
# Output Format
# For each test case, output Yes if he can complete the assignments on time. Otherwise, output No.

# You may print each character of Yes and No in uppercase or lowercase (for example, yes, yEs, YES will be considered identical).

# Constraints
# 1
# ≤
# T
# ≤
# 10
# 1≤T≤10
# 1
# ≤
# X
# ≤
# 9
# 1≤X≤9
# Sample 1:
# Input
# Output
# 2
# 7
# 9
# Yes
# No
# Explanation:
# Test case-1: He can start at 
# 7
# 7pm and finish by 
# 10
# 10 pm. Therefore he can complete the assignments.

# Test case-2: He can not complete all the 
# 3
# 3 assignments if he starts at 
# 9
# 9 pm.

# cook your dish here
T=int(input())
for i in range(T):
    X=int(input())
    if X<=7:
        print("YES")
    else:
        print("NO")