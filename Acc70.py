class Solution(object):
    def romanToInt(self, s):
        roman_dict = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        prev_value = 0

        for char in reversed(s):  # Iterate from the end of the string
            current_value = roman_dict[char]
            if current_value < prev_value:
                total -= current_value  # Subtract if smaller value precedes a larger one
            else:
                total += current_value  # Otherwise, add the value
            prev_value = current_value

        return total
for _ in range(int(input())):
    a,b,x=map(int,input().split())
    res=b-a
    r=res/x
    print(int(r))

for _ in range(int(input())):
    d,l,r=map(int,input().split())
    if l<=d<=r:
        print("Take second dose now")
    elif d>r:
        print("Too Late")
    else:
        print("Too Early")