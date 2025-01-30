# Binary Battles
for _ in range(int(input())):
    N, A, B = map(int, input().split())
    
    # Calculate the number of rounds
    rounds = N.bit_length() - 1
    
    # Calculate the total time
    total_time = rounds * A + (rounds - 1) * B
    
    print(total_time)

# Best of Two

for _ in range(int(input())):
    lst=list(map(int,input().split()))
    sumA=0
    sumB=0
    Alice=lst[:3]
    Alice.sort(reverse=True)
    Alice.remove(Alice[-1])
    bobs=lst[3:]
    bobs.sort(reverse=True)
    bobs.remove(bobs[-1])
    for i in Alice:
        sumA+=i
    for j in bobs:
        sumB+=j
    if sumB==sumA:
        print("tie")
    elif sumA>sumB:
        print("Alice")
    else:
        print("Bob")
    
    
def update_scores(a, b):
    global winner, final_lead, total_a, total_b
    total_a += a
    total_b += b
    
    if total_a > total_b:
        lead = total_a - total_b
        if lead > final_lead:
            final_lead = lead
            winner = 1
    else:
        lead = total_b - total_a
        if lead > final_lead:
            final_lead = lead
            winner = 2


# The Lead Game
def main():
    global winner, final_lead, total_a, total_b
    winner = 0
    final_lead = 0
    total_a, total_b = 0, 0
    
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        update_scores(a, b)
    
    print(winner, final_lead)

if __name__ == "__main__":
    main()

# finding sub array
l=[1,8,9]
n=len(l)
ans=[]
for i in range(n):
  for j in range(i,n):
    temp=[]
    for k in range(i,j+1):
      temp.append(l[k])
    ans.append(temp)
print(ans)

# finding sub string
s='prasad'
n=len(s)
ans=[]
for i in range(n):
    for j in range(i,n):
        temp=''
        for k in range(i,j+1):
            temp+=s[k]
        ans.append(temp)
print(ans)