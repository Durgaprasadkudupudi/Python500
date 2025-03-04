for _ in range(int(input())):
    x,y=map(int,input().split())
    if x>y*10:
        print("YES")
    else:
        print("NO")

for _ in range(int(input())):
    x,y=map(int,input().split())
    print(abs(x-y))

# Read inputs
X, Y = map(float, input().split())

# Check withdrawal conditions
if X % 5 == 0 and X + 0.50 <= Y:
    Y -= (X + 0.50)

# Print the final balance with two decimal precision
print(f"{Y:.2f}")


# cook your dish here
for _ in range(int(input())):
    x=int(input())
    if x>20:
        print("HOT")
    else:
        print("cold")