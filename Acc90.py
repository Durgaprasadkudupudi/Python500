#write a function that accepts three parameters:two positive integers r and unit,and a positive intiger array arr of size n
# r represents the number of rats present in an area
#unit represent the amount of food each rat consumes

#Each element of the array arr represents the amount of food in the each house, where index of th array corresponds to the house number
# where index of the array corresponds to the number


# the function should determine the minimum number of houses required to provide enough food to theb cats

# constraints

#return -1 if the array is null

# return 0 if the total amount  of food from all hour=ses is not sufficient for all the rats

# computed values lie within the integer range

#Example

# input

# r:7

# unit:2

# n:8

# arr:[2,8,3,5,7,4,1,2]

# output:4

def  Calculatefood(r,unit,arr):
    total_food=r*unit
    count=0
    foodtillnow=0

    if len(arr)==0:
        return -1
    elif len(arr)!=0:
        for i in arr:
            if total_food>foodtillnow:
                foodtillnow+=i
                count+=1
        print(count)
    else:
        return 0
    
arr=[3,6,8,31,21]
Calculatefood(7,4,arr)

