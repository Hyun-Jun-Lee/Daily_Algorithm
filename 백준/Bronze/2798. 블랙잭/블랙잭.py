import sys

n, m = map(int, sys.stdin.readline().split())
card = list(map(int,sys.stdin.readline().split()))
    
result = 0

for i in range(len(card)):
    for j in range(i+1, len(card)):
        for k in range(j+1, len(card)):
            sum_val = card[i] + card[j] + card[k]
            if sum_val <=m:
                result = max(result, sum_val)

print(result)

