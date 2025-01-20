T = int(input())
for _ in range(T):
    X, Y, Z = map(int, input().split())
    time_to_reach = Y / X
    wait_time = max(0, Z - time_to_reach)
    print(int(wait_time))

T = int(input())
for _ in range(T):
    
    rating=0
    X, Y = map(int, input().split())
    
    if X >= Y:
       print(0)
    else:
        difference = Y - X
        # Calculate the minimum number of games needed
        games = (difference + 7) // 8
        print(games)
                