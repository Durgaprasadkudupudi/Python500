# cook your dish here
for _ in range(int(input())):
    N = int(input())
    P = list(map(int, input().split()))
    
    # Create a list to count the occurrences of each preferred group size
    count = [0] * (N + 1)
    
    # Count the number of people for each preferred group size
    for group_size in P:
        count[group_size] += 1
    
    # Flag to determine if all group sizes can be satisfied
    happy = True

    # Iterate over possible group sizes
    for group_size in range(2, N + 1):
        # Check if the count of people preferring this group size is divisible by the group size
        if count[group_size] % group_size != 0:
            happy = False
            break

    # Output the result for the test case
    if happy:
        print("YES")
    else:
        print("NO")