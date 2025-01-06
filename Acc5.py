
# Exams
# In Chefland, there are 
# X
# X schools, and each school has 
# Y
# Y students.
# The year end results are in and a total of 
# Z
# Z students passed the exams.

# Assuming that all students appeared for the exams, find whether the number of students who passed in Chefland was strictly greater than 
# 50
# %
# 50%.

# Input Format
# The first line of input will contain a single integer 
# T
# T, denoting the number of test cases.
# Each test case consists of three space-separated integers 
# X
# ,
# Y
# ,
# X,Y, and 
# Z
# Z, as mentioned in the statement.
# Output Format
# For each test case, output on a new line, YES, if the total number of students who passed in Chefland was strictly greater than 
# 50
# %
# 50%, otherwise print NO.

# You may print each character of the string in uppercase or lowercase (for example, the strings YES, yEs, yes, and yeS will all be treated as identical).

# Constraints
# 1
# ≤
# T
# ≤
# 2
# ⋅
# 1
# 0
# 4
# 1≤T≤2⋅10 
# 4
 
# 1
# ≤
# X
# ≤
# 5
# 1≤X≤5
# 1
# ≤
# Y
# ≤
# 50
# 1≤Y≤50
# 0
# ≤
# Z
# ≤
# X
# ⋅
# Y
# 0≤Z≤X⋅Y
# Sample 1:
# Input
# Output
# 4
# 2 10 12
# 2 10 3
# 1 5 3
# 3 6 9
# YES
# NO
# YES
# NO
# Explanation:
# Test case 
# 1
# 1: The total number of students appeared were 
# 2
# ⋅
# 10
# =
# 20
# 2⋅10=20. The number of students passed were 
# 12
# 12.
# Thus, number of students who passed are 
# 60
# %
# 60%, which is strictly greater than 
# 50
# %
# 50%.

# Test case 
# 2
# 2: The total number of students appeared were 
# 2
# ⋅
# 10
# =
# 20
# 2⋅10=20. The number of students passed were 
# 3
# 3.
# Thus, number of students who passed are 
# 15
# %
# 15%, which is less than 
# 50
# %
# 50%.

# Test case 
# 3
# 3: The total number of students appeared were 
# 1
# ⋅
# 5
# =
# 5
# 1⋅5=5. The number of students passed were 
# 3
# 3.
# Thus, number of students who passed are 
# 60
# %
# 60%, which is strictly greater than 
# 50
# %
# 50%.

# Test case 
# 4
# 4: The total number of students appeared were 
# 3
# ⋅
# 6
# =
# 18
# 3⋅6=18. The number of students passed were 
# 9
# 9.
# Thus, number of students who passed are 
# 50
# %
# 50%, which is equal to 
# 50
# %
# 50%.

# cook your dish here
T=int(input())
for i in range(T):
    X,Y,Z=map(int,input().split())
    if( Z/(X*Y))*100>50:
        print("yes")
    else:
        print("no")


# Chef recently joined a new company. In this company, employees work X hours each day from Monday to Thursday. On Friday, which is called Chill Day, employees work for only Y hours, where Y < X. Saturday and Sunday are holidays.

# Your task is to determine the total number of working hours in one week.

# Input Format
# The first line contains a single integer T — the number of test cases.
# Each test case consists of a single line containing two space-separated integers X and Y:
# X — the number of working hours from Monday to Thursday (each day).
# Y — the number of working hours on Friday.
# Output Format
# For each test case, output a single integer — the total number of working hours in one week.

# Constraints
# 1
# ≤
# 𝑇
# ≤
# 100
# 1≤T≤100
# 2
# ≤
# 𝑋
# ≤
# 12
# 2≤X≤12
# 1
# ≤
# 𝑌
# <
# 𝑋
# 1≤Y<X
# Calculation
# Total working hours for one week can be calculated as:

# Total Hours
# =
# (
# 4
# ×
# 𝑋
# )
# +
# 𝑌
# Total Hours=(4×X)+Y
# Where:

# 4
# ×
# 𝑋
# 4×X is the total hours from Monday to Thursday.
# 𝑌
# Y is the hours worked on Friday.
# Sample Input
# Copy code
# 3  
# 10 5  
# 12 2  
# 8 7  
# Sample Output
# Copy code
# 45  
# 50  
# 39  
# Explanation
# Test Case 1:

# 10
# ×
# 4
# +
# 5
# =
# 40
# +
# 5
# =
# 45
# 10×4+5=40+5=45
# Test Case 2:

# 12
# ×
# 4
# +
# 2
# =
# 48
# +
# 2
# =
# 50
# 12×4+2=48+2=50
# Test Case 3:

# 8
# ×
# 4
# +
# 7
# =
# 32
# +
# 7
# =
# 39
# 8×4+7=32+7=39

# cook your dish here
T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    if Y<X:
        total=X*4+Y
    print(total)



# Mahasena
# Kattapa, as you all know was one of the greatest warriors of his time. The kingdom of Maahishmati had never lost a battle under him (as army-chief), and the reason for that was their really powerful army, also called as Mahasena.

# Kattapa was known to be a very superstitious person. He believed that a soldier is "lucky" if the soldier is holding an even number of weapons, and "unlucky" otherwise. He considered the army as "READY FOR BATTLE" if the count of "lucky" soldiers is strictly greater than the count of "unlucky" soldiers, and "NOT READY" otherwise.

# Given the number of weapons each soldier is holding, your task is to determine whether the army formed by all these soldiers is "READY FOR BATTLE" or "NOT READY".

# Note: You can find the number of soldiers with an even number of weapons by dividing the count of soldiers with even number of weapons by 2.
# Explanation:
# Example 1: For the first example, N = 1 and the array A = [1]. There is only 1 soldier and he is holding 1 weapon, which is odd. The number of soldiers holding an even number of weapons = 0, and number of soldiers holding an odd number of weapons = 1. Hence, the answer is "NOT READY" since the number of soldiers holding an even number of weapons is not greater than the number of soldiers holding an odd number of weapons.

N = int(input())
A = list(map(int, input().split()))  
lstE = []
lstO = []

for num in A:
    if num % 2 == 0:
        lstE.append(num)
    else:
        lstO.append(num)

if len(lstE) > len(lstO):
    print("READY FOR BATTLE")
else:
    print("NOT READY")


# CRED Coins
# For each bill you pay using CRED, you earn 
# X
# X CRED coins.
# At CodeChef store, each bag is worth 
# 100
# 100 CRED coins.

# Chef pays 
# Y
# Y number of bills using CRED. Find the maximum number of bags he can get from the CodeChef store.

# Input Format
# First line will contain 
# T
# T, number of test cases. Then the test cases follow.
# Each test case contains of a single line of input, two integers 
# X
# X and 
# Y
# Y.
# Output Format
# For each test case, output in a single line - the maximum number of bags Chef can get from the CodeChef store.

# Explanation:
# Test Case 
# 1
# 1: For each bill payment, one receives 
# 10
# 10 CRED coins. Chef pays 
# 10
# 10 bills using CRED. Thus, he receives 
# 100
# 100 CRED coins. Chef can get 
# 1
# 1 bag from the CodeChef store using these coins.

# Test Case 
# 2
# 2: For each bill payment, one receives 
# 20
# 20 CRED coins. Chef pays 
# 4
# 4 bills using CRED. Thus, he receives 
# 80
# 80 CRED coins. Chef cannot get any bag from the CodeChef store using these coins.

# Test Case 
# 3
# 3: For each bill payment, one receives 
# 70
# 70 CRED coins. Chef pays 
# 7
# 7 bills using CRED. Thus, he receives 
# 490
# 490 CRED coins. Chef can get at most 
# 4
# 4 bags from the CodeChef store using these coins.

# cook your dish here
T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    Z=X*Y
    bags=Z//100
    print(bags)



# Water Filling
# Chef has three water bottles. At any point, if at least two of them are empty, she will fill them up. But if at most one bottle is empty, she will wait, and not fill them up now.

# You are given three integers - 
# B
# 1
# ,
# B
# 2
# ,
# B 
# 1
# ​
#  ,B 
# 2
# ​
#  , and 
# B
# 3
# B 
# 3
# ​
#  .
# If 
# B
# 1
# =
# 1
# B 
# 1
# ​
#  =1, it means that the first bottle is full.
# If 
# B
# 1
# =
# 0
# B 
# 1
# ​
#  =0, it means that the first bottle is empty.
# Similarly, 
# B
# 2
# B 
# 2
# ​
#   denotes whether the second bottle is full or empty, and 
# B
# 3
# B 
# 3
# ​
#   denotes it for the third bottle.

# Output "Water filling time", if Chef has to fill the bottles now. If not, output "Not now".

T = int(input())
for _ in range(T):
    B1, B2, B3 = map(int, input().split())
    if B1 + B2 + B3 <= 1:
        print("Water filling time")
    else:
        print("Not now")