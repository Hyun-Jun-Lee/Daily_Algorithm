import sys

n, k = map(int, sys.stdin.readline().split())
coin = []
cnt = 0

for _ in range(n):
    coin.append(int(sys.stdin.readline()))

# 내림차순 정렬
coin.sort(reverse=True)


for c in coin:
    if k ==0:
        break
    # 쓰인 동전 횟수
    cnt += k//c
    # 현재 코인으로 나누고 남은 돈
    k %= c

print(cnt)