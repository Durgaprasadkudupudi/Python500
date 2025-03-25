for _ in range(int(input())):
    x,y=map(int,input().split())
    res=4*x+y
    print(res)

    N=int(input())
l=list(map(int,input().split()))
lucky=0
unlucky=0
for i in l:
    if i%2==0:
        lucky+=1
    else:
        unlucky+=1
if lucky>unlucky:
    print("READY FOR BATTLE")
else:
    print("NOT READY")