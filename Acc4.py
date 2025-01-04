# count words

a="hello world how are you"

lst=a.split()
print(len(lst))

# find the GCD

a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
lst=[]
maximum=max(a,b)
for i in range(1,maximum+1):
    if a%i==0 and b%i==0:
        lst.append(i)
lst.sort(reverse=True)
print(lst[0])


#lucky 7

a="rtyrturuytiyit7ti"
b=a[6]
print(b)


#perfect number
a=int(input("Enter the number"))
sum=0
for i in range(1,a):
    if a%i==0:
        sum=sum+i
if sum==a:
    print("Perfect number")
else:
    print("Not a perfect number")