for _ in range(int(input())):
    N, A = map(int, input().split())
    print(min(A, N - A))

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        bracket_map = {
            "}": "{", ")" : "(", "]": "["
        }
        opening_brackets = set(["(", "[", "{"])
        
        for x in s:
            if x in opening_brackets:
                stack.append(x)
            elif stack and stack[-1] == bracket_map[x]:
                stack.pop()
            else:
                return False
        
        if stack:
            return False
        else:
            return True
        
# T = O(N)
# S = O(N)

import sys
import math

def simple_sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for start in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[start]:
            for multiple in range(start*start, limit + 1, start):
                is_prime[multiple] = False
    return [num for num, prime in enumerate(is_prime) if prime]

def segmented_sieve(m, n):
    limit = int(math.sqrt(n)) + 1
    primes = simple_sieve(limit)
    
    is_prime = [True] * (n-m+1)
    if m == 1:
        is_prime[0] = False  # 1 is not a prime number

    for prime in primes:
        start = max(prime*prime, m + (prime - m % prime) % prime)
        for j in range(start, n + 1, prime):
            is_prime[j - m] = False
    
    return [i for i, prime in enumerate(is_prime, m) if prime]

def main():
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        m = int(data[index])
        n = int(data[index+1])
        index += 2
        primes_in_range = segmented_sieve(m, n)
        results.append(primes_in_range)
    
    for i, primes in enumerate(results):
        for prime in primes:
            print(prime)
        if i < t - 1:
            print()

if __name__ == "__main__":
    main()


for _ in range(int(input())):
    a, b, x = map(int, input().split())
    
    # Check if the difference is divisible by 2*x
    if (a - b) % (2 * x) == 0:
        print("YES")
    else:
        print("NO")



def digit_sum(n):
    return sum(int(digit) for digit in str(n))

def find_next_different_parity(N):
    original_parity = digit_sum(N) % 2  # 0 for even, 1 for odd
    X = N + 1
    
    while digit_sum(X) % 2 == original_parity:
        X += 1  # Keep increasing X until we find different parity

    return X

# Read input
T = int(input())  # Number of test cases
for _ in range(T):
    N = int(input())
    print(find_next_different_parity(N))