T = int(input())  # Number of test cases

for _ in range(T):
    N = int(input())  # Number of submissions
    max_scores = [0] * 8  # To store max scores for problems 1 to 8

    for _ in range(N):
        p, s = map(int, input().split())  # Read problem number and score
        
        if 1 <= p <= 8:  # Only consider scorable problems
            max_scores[p - 1] = max(max_scores[p - 1], s)

    total_score = sum(max_scores)  # Sum up the best scores
    print(total_score)
