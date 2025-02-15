# cook your dish here
for _ in range(int(input())):
    X,Y=map(int,input().split())
    if X>Y:
        print("A")
    else:
        print("B")

for _ in range(int(input())):
    X,Y=map(int,input().split())
    print(X-Y)

# cook your dish here
for _ in range(int(input())):
    X,Y=map(int,input().split())
    if X>=Y:
        print(X)
    else:
        print(Y)

class Solution(object):
    def findAnagrams(self, s, p):
        def fun(dicia, dicib):
            if len(dicia) != len(dicib):
                return False
            for i in dicia:
                if i not in dicib or dicia[i] != dicib[i]:
                    return False
            return True

        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        dicia = {}
        dicib = {}

        # Populate frequency dictionary for pattern p
        for i in p:
            if i in dicib:
                dicib[i] += 1
            else:
                dicib[i] = 1

        l = 0
        ans = []
        n = len(s)
        k = len(p)

        for r in range(n):
            val = s[r]
            if val in dicia:
                dicia[val] += 1
            else:
                dicia[val] = 1  # Fixed typo (was `dici[val]`)

            # Ensure window size is always k
            if r - l + 1 > k:  
                lval = s[l]
                dicia[lval] -= 1
                if dicia[lval] == 0:
                    del dicia[lval]  # Use `del` instead of `.pop()`
                l += 1

            # If window size equals pattern length, check for anagram
            if r - l + 1 == k:
                if fun(dicia, dicib):
                    ans.append(l)

        return ans