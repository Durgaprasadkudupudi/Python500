def arm(num):
    digits=str(num)
    n_digits=len(digits)
    temp=0
    for d in digits:
        temp += int(d) ** n_digits
    return temp== num
num= int(input("enter:"))
print(arm(num))