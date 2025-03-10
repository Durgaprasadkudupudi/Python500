# cook your dish here
for _ in range(int(input())):
    N=int(input())
    M=str(N)
    sum=int(M[0])+int(M[-1])
    print(sum)

(n, k) = map(int, input().split())

ans = 0

for i in range(n):
	x = int(input())
	if x % k == 0:
		ans += 1

print(ans)	


# cook your dish here

a,b,c,d=map(int,input().split())
list2=[]
list2.append(a)
list2.append(b)
list2.append(c)
list2.append(d)
count=0
for i in list2:
    if i>=10:
        count+=1
print(count)
