def solve():
    x, y, z = map(int, input().split())
    
    # Calculate the remaining weight the truck can carry
    remaining_weight = z - y
    
    # Calculate the maximum number of mangoes
    if remaining_weight < 0 :
        print(0)
    else:
        max_mangoes = remaining_weight // x
        print(max_mangoes)

# Handle multiple test cases
t = int(input())
for _ in range(t):
    solve()


for _ in range(int(input())):
    r1,r2,r3=map(int,input().split())
    if r1>r2+r3 or r2>r1+r3 or r3>r1+r2:
        print("yes")
    else:
        print("NO")