import sys

n = map(int, sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

# 진짜 약수들만 주어지기 때문에
#가장 큰 값과 작은 값을 곱하면 진짜 수를 구할 수 있음
max_num = max(num)
min_num = min(num)

print(max_num * min_num)