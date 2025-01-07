# Sale Season
# It's the sale season again and Chef bought items worth a total of 
# X
# X rupees. The sale season offer is as follows:

# if 
# X
# ≤
# 100
# X≤100, no discount.
# if 
# 100
# <
# X
# ≤
# 1000
# 100<X≤1000, discount is 
# 25
# 25 rupees.
# if 
# 1000
# <
# X
# ≤
# 5000
# 1000<X≤5000, discount is 
# 100
# 100 rupees.
# if 
# X
# >
# 5000
# X>5000, discount is 
# 500
# 500 rupees.
# Find the final amount Chef needs to pay for his shopping.

# Input Format
# The first line of input will contain a single integer 
# T
# T, denoting the number of test cases.
# Each test case consists of single line of input containing an integer 
# X
# X.

# Explanation:
# Test case 
# 1
# 1: Since 
# X
# ≤
# 100
# X≤100, there is no discount.

# Test case 
# 3
# 3: Here, 
# X
# =
# 250
# X=250. Since 
# 100
# <
# 250
# ≤
# 1000
# 100<250≤1000, discount is of 
# 25
# 25 rupees. Therefore, Chef needs to pay 
# 250
# −
# 25
# =
# 225
# 250−25=225 rupees.

T= int(input())
for i in range(T):
    X=int(input())
    if X<=100:
        print(X)
    elif 100 < X <=1000:
        dis=X-25
        print(dis)
    elif 1000< X<=5000:
        dis=X-100
        print(dis)
    elif X>5000:
        print(X-500)

# Minimum Pizzas
# Each pizza consists of 
# 4
# 4 slices. There are 
# N
# N friends and each friend needs exactly 
# X
# X slices.

# Find the minimum number of pizzas they should order to satisfy their appetite.

# Input Format
# The first line of input will contain a single integer 
# T
# T, denoting the number of test cases.
# Each test case consists of two integers 
# N
# N and 
# X
# X, the number of friends and the number of slices each friend wants respectively.
# Output Format
# For each test case, output the minimum number of pizzas required.

# Explanation:
# Test case 
# 1
# 1: There is only 
# 1
# 1 friend who requires 
# 5
# 5 slices. If he orders 
# 1
# 1 pizza, he will get only 
# 4
# 4 slices. Thus, at least 
# 2
# 2 pizzas should be ordered to have required number of slices.

# Test case 
# 2
# 2: There are 
# 2
# 2 friends who require 
# 6
# 6 slices each. Thus, total 
# 12
# 12 slices are required. To get 
# 12
# 12 slices, they should order 
# 3
# 3 pizzas.

# Test case 
# 3
# 3: There are 
# 4
# 4 friends who require 
# 3
# 3 slices each. Thus, total 
# 12
# 12 slices are required. To get 
# 12
# 12 slices, they should order 
# 3
# 3 pizzas.

# Test case 
# 4
# 4: There are 
# 3
# 3 friends who require 
# 5
# 5 slices each. Thus, total 
# 15
# 15 slices are required. To get 
# 15
# 15 slices, they should order at least 
# 4
# 4 pizzas.


# cook your dish here

T=int(input())
for i in range(T):
    N,X=map(int,input().split())
    total=N*X
    lst=[]
    for j in range(1,total+1,4):
        lst.append(j)
        
        
        
    print(len(lst))

# Chefland Games
# In Chefland, a tennis game involves 
# 4
# 4 referees.
# Each referee has to point out whether he considers the ball to be inside limits or outside limits. The ball is considered to be IN if and only if all the referees agree that it was inside limits.

# Given the decision of the 
# 4
# 4 referees, help Chef determine whether the ball is considered inside limits or not.

# Input Format
# The first line of input will contain a single integer 
# T
# T, denoting the number of test cases.
# Each test case consists of a single line of input containing 
# 4
# 4 integers 
# R
# 1
# ,
# R
# 2
# ,
# R
# 3
# ,
# R
# 4
# R 
# 1
# ​
#  ,R 
# 2
# ​
#  ,R 
# 3
# ​
#  ,R 
# 4
# ​
#   denoting the decision of the respective referees.
# Here 
# R
# R can be either 
# 0
# 0 or 
# 1
# 1 where 
# 0
# 0 would denote that the referee considered the ball to be inside limits whereas 
# 1
# 1 denotes that they consider it to be outside limits.

# Output Format
# For each test case, output IN if the ball is considered to be inside limits by all referees and OUT otherwise.

# The checker is case-insensitive so answers like in, In, and IN would be considered the same.

# Explanation:
# Test case 
# 1
# 1: Referees 
# 1
# 1 and 
# 2
# 2 do not consider the ball to be IN. Thus, the ball is OUT.

# Test case 
# 2
# 2: All referees consider the ball to be IN. Thus, the ball is IN.

# Test case 
# 3
# 3: Referee 
# 4
# 4 does not consider the ball to be IN. Thus, the ball is OUT.

# Test case 
# 4
# 4: No referee considers the ball to be IN. Thus, the ball is OUT.

T=int(input())
for i in range(T):
    R1,R2,R3,R4=map(int,input().split())
    if R1==0 and R2==0 and R3==0 and R4==0:
        print("IN")
    else:
        print("OUT")


# A problem setter is called an expert if at least 
# 50
# %
# 50% of their problems are approved by Chef.

# Munchy submitted 
# X
# X problems for approval. If 
# Y
# Y problems out of those were approved, find whether Munchy is an expert or not.

# Input Format
# The first line of input will contain a single integer 
# T
# T, denoting the number of test cases.
# Each test case consists of a two space-separated integers 
# X
# X and 
# Y
# Y - the number of problems submitted and the number of problems that were approved by Chef.
# Output Format
# For each test case, output on a new line YES, if Munchy is an expert. Otherwise, print NO.

# The output is case-insensitive. Thus, the strings YES, yes, yeS, and Yes are all considered the same.

# Explanation:
# Test case 
# 1
# 1: We are given that 
# 3
# 3 out of 
# 5
# 5 problems were approved. Thus, 
# 60
# %
# 60% of the problems were approved. Since at least 
# 50
# %
# 50% of the problems were approved, Munchy is an expert.

# Test case 
# 2
# 2: We are given that 
# 1
# 1 out of 
# 1
# 1 problems were approved. Thus, 
# 100
# %
# 100% of the problems were approved. Since at least 
# 50
# %
# 50% of the problems were approved, Munchy is an expert.

# Test case 
# 3
# 3: We are given that 
# 1
# 1 out of 
# 4
# 4 problems were approved. Thus, 
# 25
# %
# 25% of the problems were approved. Since at least 
# 50
# %
# 50% of the problems were not approved, Munchy is not an expert.

# Test case 
# 4
# 4: We are given that 
# 1
# 1 out of 
# 2
# 2 problems were approved. Thus, 
# 50
# %
# 50% of the problems were approved. Since at least 
# 50
# %
# 50% of the problems were approved, Munchy is an expert.

T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    if (Y/X)*100>=50:
        print("YES")
    else:
        print("NO")
