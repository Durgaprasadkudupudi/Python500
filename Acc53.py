n = 3
m = 27
l = 1
h = m
ans = -1

while l <= h:
    mid = (l + h) // 2
    res = mid * n  # Compute mid * n

    if res == m:  # Found the answer
        ans = mid
        break  # Exit loop when we find the correct mid

    if res < m:  # If mid * n is less than m, move right
        l = mid + 1
    else:  # If mid * n is greater than m, move left
        h = mid - 1

print(ans)  # Print the found value or -1 if not found


# cook your dish here

x,n,m=map(int,input().split())
total=x+m
if total<n:
    print('NO')
else:
    print("YES")

for _ in range(int(input())):
    x,y=map(int,input().split())
    tkil=x*5
    if tkil>=y:
        print("YES")
    else:
        print("NO")