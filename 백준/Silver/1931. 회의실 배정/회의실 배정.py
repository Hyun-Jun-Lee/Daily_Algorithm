import sys

n = int(sys.stdin.readline())

m_time = []

for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    m_time.append((start, end))

# 빨리 끝나는 시간 1차 정렬 후 빨리 시작하는 시간으로 정렬
# [(1,4),(3,5),(0,6),(5,7)]
m_time = sorted(m_time, key=lambda x:(x[1], x[0]))

end_time = 0
cnt = 0
for t in m_time:
    # 시작 시간이 끝나는 시간보다 크거나 같다면
    if t[0] >= end_time:
        end_time = t[1]
        cnt += 1
print(cnt)

