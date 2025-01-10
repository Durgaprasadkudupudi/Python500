# minimum pizzas required
import math
T = int(input())
for i in range(T):
    N, X = map(int, input().split())
    if X >= N:
        print(0)
    else:
        diff = N - X
        print(math.ceil(diff / 4))

# Bike or car timings
T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    if X==Y:
        print("same")
    elif  X>Y:
        print("car")
    elif Y>X:
        print("bike")

# Is the Score Consistent

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    C, D = map(int, input().split())
    
    if C >= A and D >= B:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")