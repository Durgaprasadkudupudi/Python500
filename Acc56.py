# Function to calculate new profit after increasing selling price by 10%
def new_profit(x, y):
    # Calculate cost price
    cost_price = x - y  
    # New selling price after 10% increase
    new_selling_price = x + (x * 10) // 100  
    # New profit
    return new_selling_price - cost_price  

# Read number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    x, y = map(int, input().split())
    print(new_profit(x, y))


for _ in range(int(input())):
    k,x=map(int,input().split())
    print(k-x)


# cook your dish here
for _ in range(int(input())):
    n,x=map(int,input().split())
    half=n/2
    if x>=half:
        print("YES")
    else:
        print("NO")

# cook your dish here
# cook your dish here
for _ in range(int(input())):
    n,x=map(int,input().split())
    
    print(n%x)

for _ in range(int(input())):
    x,y=map(int,input().split())
    if x<y:
        print("NO")
    else:
        print("YES")
    
    