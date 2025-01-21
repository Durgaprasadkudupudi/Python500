def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    T = int(data[0])  # Read number of test cases
    index = 1

    dna = "ATCG"
    comp = "TAGC"

    for _ in range(T):
        n = int(data[index])  # Read length of the string (not used)
        s = data[index + 1]   # Read the DNA sequence
        index += 2

        result = []
        for char in s:
            for i in range(4):
                if char == dna[i]:
                    result.append(comp[i])
                    break

        print("".join(result))

if __name__ == "__main__":
    main()



for _ in range(int(input())):
    N, X, K = map(int, input().split())

  
    count = min(N, K // X)
    
    print(count)