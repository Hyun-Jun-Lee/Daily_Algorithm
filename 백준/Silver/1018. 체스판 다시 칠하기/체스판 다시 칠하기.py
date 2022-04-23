import sys

n, m = map(int, sys.stdin.readline().split())
fields = []
cnt = []

for  _ in range(n):
    fields.append(sys.stdin.readline())

# 체스판에서 시작점을 찾기 위한 반복문
for a in range(n-7):
    for b in range(m-7):
        # w로 시작할 때 다시 칠해야 하는 개수
        color_w = 0
        # b 로 시작할 때 다시 칠해야 하는 개수
        color_b = 0
        # 현재 행 i, 현재 열 j
        for i in range(a, a+8):
            for j in range(b, b+8):
                # 현재 행,열의 합이 짝수 -> 시작점과 색 같아야함
                if (i+j) %2 ==0:
                    # 시작이 W인데 짝수 번째가 W가 아닌경우
                    if fields[i][j] != 'W':
                        color_w += 1
                    # 시작이 B인데 짝수 번째가 B가 아닌경우
                    if fields[i][j] != 'B':
                        color_b += 1
                # 합이 홀수 -> 시작점과 색 달라야함
                else:
                    if fields[i][j] != 'B':
                        color_w += 1
                    if fields[i][j] != 'W':
                        color_b += 1
        cnt.append(min(color_w,color_b))

print(min(cnt))
