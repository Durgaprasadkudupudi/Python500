# Bus Seat Numbering


T=int(input())
lowD=[1,2,3,4,5,6,7,8,9,10]
lowS=[11,12,13,14,15]
upperD=[16,17,18,19,20,21,22,23,24,25]
upperS=[26,27,28,29,30]
for i in range(T):
    N=int(input())
    if N in lowD:
        print("Lower Double")
    elif N in lowS:
        print("Lower Single")
    elif N in upperS:
        print("Upper Single")
    else:
        print("Upper Double")
    
# Discus Throw
# In discus throw, a player is given 
# 3
# 3 throws and the throw with the longest distance is regarded as their final score.

# cook your dish here
for i in range(int(input())):
    A,B,C=map(int,input().split())
    if A>=B and A>=C:
        print(A)
    elif B>=A and B>=C:
        print(B)
    else:
        print(C)


# maximise ingrediants
for i in range(int(input())):
    a,b,c,d=map(int,input().split())
    ing1=max(a,b)
    ing2=max(c,d)
    tsum=ing2+ing1
    print(tsum)


# Watching Movies at 2x


X,Y=map(int,input().split())
total=((Y/2)+(X-Y))
print(int(total))
   