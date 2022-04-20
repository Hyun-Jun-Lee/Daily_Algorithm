import sys

n = int(sys.stdin.readline())
size = []

for _ in range(n):
    w, h = map(int, sys.stdin.readline().split())
    size.append((w,h))
    
for i in size:
    rank = 1
    for j in size:
        if i[0] < j[0] and i[1]< j[1]:
            rank += 1
    print(rank, end=' ')