
# Chef and NextGen
# Chef is currently working for a secret research group called NEXTGEN. While the rest of the world is still in search of a way to utilize Helium-3 as a fuel, NEXTGEN scientists have been able to achieve 2 major milestones:

# Finding a way to make a nuclear reactor that will be able to utilize Helium-3 as a fuel
# Obtaining every bit of Helium-3 from the moon's surface
# Moving forward, the project requires some government funding for completion, which comes under one condition: to prove its worth, the project should power Chefland by generating at least 
# A
# A units of power each year for the next 
# B
# B years.

# Help Chef determine whether the group will get funded assuming that the moon has 
# X
# X grams of Helium-3 and 
# 1
# 1 gram of Helium-3 can provide 
# Y
# Y units of power.

# Input Format
# The first line of input contains an integer 
# T
# T, the number of testcases. The description of 
# T
# T test cases follows.
# Each test case consists of a single line of input, containing four space-separated integers 
# A
# ,
# B
# ,
# X
# ,
# Y
# A,B,X,Y respectively.
# Output Format
# For each test case print on a single line the answer — Yes if NEXTGEN satisfies the government's minimum requirements for funding and No otherwise.

# You may print each character of the answer string in either uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

# Explanation:
# Test case 
# 1
# 1: Chefland requires 
# A
# =
# 1
# A=1 units of power for the next 
# B
# =
# 2
# B=2 years. In total, the moon must be capable of providing 
# A
# ⋅
# B
# =
# 2
# A⋅B=2 units of power. There are in total 
# X
# =
# 3
# X=3 grams of Helium-3 on the moon which is capable of providing 
# X
# ⋅
# Y
# =
# 12
# X⋅Y=12 units of power. 
# 12
# >
# 2
# 12>2, so the project satisfies the minimum requirements for funding. Thus, the answer is Yes.

# Test case 
# 2
# 2: The total amount of power needed by Chefland is 
# A
# ⋅
# B
# =
# 12
# A⋅B=12, whereas the total that can be provided by the Helium-3 present on the moon is 
# X
# ⋅
# Y
# =
# 2
# X⋅Y=2, which is insufficient to receive funding, so the answer is No.

# Test case 
# 3
# 3: The total amount of power needed by Chefland is 
# A
# ⋅
# B
# =
# 2
# ⋅
# 18
# =
# 36
# A⋅B=2⋅18=36, and the total that can be provided by the Helium-3 present on the moon is 
# X
# ⋅
# Y
# =
# 9
# ⋅
# 4
# =
# 36
# X⋅Y=9⋅4=36, which is sufficient to receive funding, so the answer is Yes.

# Test case 
# 4
# 4: The total amount of power needed by Chefland is 
# A
# ⋅
# B
# =
# 1
# ⋅
# 100
# =
# 100
# A⋅B=1⋅100=100, and the total that can be provided by the Helium-3 present on the moon is 
# X
# ⋅
# Y
# =
# 2
# ⋅
# 49
# =
# 98
# X⋅Y=2⋅49=98, which is insufficient to receive funding, so the answer is No.

# cook your dish here

T=int(input())
for i in range(T):
    A,B,X,Y=map(int,input().split())
    if X*Y >= A*B:
        print("yes")
    else:
        print("no")


# Problem Statement: Sugarcane Juice Business
# Alice was enjoying a glass of sugarcane juice and started thinking about how the juicer runs his business. She noted the following facts:

# The juicer sells each glass of sugarcane juice for 50 coins.
# He spends 20% of his total income on buying sugarcane.
# He spends 20% of his total income on buying salt and mint leaves.
# He spends 30% of his total income on shop rent.
# Alice wants to know the profit (in coins) the juicer makes after covering all his expenses when he sells N glasses of sugarcane juice.

# Input Format:
# The first line of input contains a single integer T — the number of test cases.
# The next T lines contain a single integer N — the number of glasses of sugarcane juice sold.

# Explanation:
# Test Case 1:
# The juicer sells 2 glasses of sugarcane juice.

# Total income = 
# 50
# ×
# 2
# =
# 100
# 50×2=100 coins.
# He spends 20 coins on sugarcane, 20 coins on salt and mint leaves, and 30 coins on rent.
# Therefore, the profit is:
# 100
# −
# (
# 20
# +
# 20
# +
# 30
# )
# =
# 30
#  coins
# 100−(20+20+30)=30 coins
# Test Case 2:
# The juicer sells 4 glasses of sugarcane juice.

# Total income = 
# 50
# ×
# 4
# =
# 200
# 50×4=200 coins.
# He spends 40 coins on sugarcane, 40 coins on salt and mint leaves, and 60 coins on rent.
# Therefore, the profit is:
# 200
# −
# (
# 40
# +
# 40
# +
# 60
# )
# =
# 60
#  coins
# 200−(40+40+60)=60 coins
# Test Case 3:
# The juicer sells 5 glasses of sugarcane juice.

# Total income = 
# 50
# ×
# 5
# =
# 250
# 50×5=250 coins.
# He spends 50 coins on sugarcane, 50 coins on salt and mint leaves, and 75 coins on rent.
# Therefore, the profit is:
# 250
# −
# (
# 50
# +
# 50
# +
# 75
# )
# =
# 75
#  coins
# 250−(50+50+75)=75 coins
# Test Case 4:
# The juicer sells 10 glasses of sugarcane juice.

# Total income = 
# 50
# ×
# 10
# =
# 500
# 50×10=500 coins.
# He spends 100 coins on sugarcane, 100 coins on salt and mint leaves, and 150 coins on rent.
# Therefore, the profit is:
# 500
# −
# (
# 100
# +
# 100
# +
# 150
# )
# =
# 150
#  coins
# 500−(100+100+150)=150 coins

T=int(input())
for i in range(T):
    N=int(input())
    sold=N*50
    sugarcane=(20/100)*sold
    salt= (20/100)*sold
    rent=(30/100)*sold
    total_invest=sugarcane+salt+rent
   
    profit=sold-total_invest
    print(int(profit))


#     Count the Notebooks
# You know that 
# 1
# 1 kg of pulp can be used to make 
# 1000
# 1000 pages and 
# 1
# 1 notebook consists of 
# 100
# 100 pages.

# Suppose a notebook factory receives 
# N
# N kg of pulp, how many notebooks can be made from that?

T = int(input())  # Number of test cases

for i in range(T):
    N = int(input())  
    count = 0        

    for j in range(1, N * 1000, 100):
        count += 1

    print(count)
