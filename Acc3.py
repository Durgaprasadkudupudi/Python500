# Greater Average
# You are given 
# 3
# 3 numbers 
# A
# ,
# B
# ,
# A,B, and 
# C
# C.

# Determine whether the average of 
# A
# A and 
# B
# B is strictly greater than 
# C
# C or not?

# NOTE: Average of 
# A
# A and 
# B
# B is defined as 
# (
# A
# +
# B
# )
# 2
# 2
# (A+B)
# ​
#  . For example, average of 
# 5
# 5 and 
# 9
# 9 is 
# 7
# 7, average of 
# 5
# 5 and 
# 8
# 8 is 
# 6.5
# 6.5.

# Input Format
# The first line of input will contain a single integer 
# T
# T, denoting the number of test cases.
# Each test case consists of 
# 3
# 3 integers 
# A
# ,
# B
# ,
# A,B, and 
# C
# C.
# Output Format
# For each test case, output YES if average of 
# A
# A and 
# B
# B is strictly greater than 
# C
# C, NO otherwise.

# You may print each character of the string in uppercase or lowercase (for example, the strings YeS, yEs, yes and YES will all be treated as identical).

# Constraints
# 1
# ≤
# T
# ≤
# 1000
# 1≤T≤1000
# 1
# ≤
# A
# ,
# B
# ,
# C
# ≤
# 10
# 1≤A,B,C≤10
# Sample 1:
# Input
# Output
# 5
# 5 9 6
# 5 8 6
# 5 7 6
# 4 9 8
# 3 7 2
# YES
# YES
# NO
# NO
# YES
# Explanation:
# Test case 
# 1
# 1: The average value of 
# 5
# 5 and 
# 9
# 9 is 
# 7
# 7 which is strictly greater than 
# 6
# 6.

# Test case 
# 2
# 2: The average value of 
# 5
# 5 and 
# 8
# 8 is 
# 6.5
# 6.5 which is strictly greater than 
# 6
# 6.

# Test case 
# 3
# 3: The average value of 
# 5
# 5 and 
# 7
# 7 is 
# 6
# 6 which is not strictly greater than 
# 6
# 6.

# Test case 
# 4
# 4: The average value of 
# 4
# 4 and 
# 9
# 9 is 
# 6.5
# 6.5 which is not strictly greater than 
# 8
# 8.

# Test case 
# 5
# 5: The average value of 
# 3
# 3 and 
# 7
# 7 is 
# 5
# 5 which is strictly greater than 
# 2
# 2.


T=int(input("Enter T value"))

for i in range(T):
    A,B,C=map(int,input().split())
    if (A+B)/2>C:
        print("YES")
    else:
        print("NO")



# Subscriptions
# A new TV streaming service was recently started in Chefland called the Chef-TV.

# A group of 
# N
# N friends in Chefland want to buy Chef-TV subscriptions. We know that 
# 6
# 6 people can share one Chef-TV subscription. Also, the cost of one Chef-TV subscription is 
# X
# X rupees. Determine the minimum total cost that the group of 
# N
# N friends will incur so that everyone in the group is able to use Chef-TV.

# Input Format
# The first line contains a single integer 
# T
# T — the number of test cases. Then the test cases follow.
# The first and only line of each test case contains two integers 
# N
# N and 
# X
# X — the size of the group of friends and the cost of one subscription.
# Output Format
# For each test case, output the minimum total cost that the group will incur so that everyone in the group is able to use Chef-TV.

# Constraints
# 1
# ≤
# T
# ≤
# 1000
# 1≤T≤1000
# 1
# ≤
# N
# ≤
# 100
# 1≤N≤100
# 1
# ≤
# X
# ≤
# 1000
# 1≤X≤1000
# Sample 1:
# Input
# Output
# 3
# 1 100
# 12 250
# 16 135
# 100
# 500
# 405
# Explanation:
# Test case 1: There is only one person in the group. Therefore he will have to buy 
# 1
# 1 subscription. Therefore the total cost incurred is 
# 100
# 100.
# Test case 2: There are 
# 12
# 12 people in the group. Therefore they will have to buy 
# 2
# 2 subscriptions. Therefore the total cost incurred is 
# 500
# 500.
# Test case 3: There are 
# 16
# 16 people in the group. Therefore they will have to buy 
# 3
# 3 subscriptions. Therefore the total cost incurred is 
# 405
# 405.

T = int(input())
for i in range(T):
    N, X = map(int, input().split())
    subscriptions = (N + 5) // 6  # This calculates the ceiling of N / 6
    total_cost = subscriptions * X
    print(total_cost)