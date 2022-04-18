n = list(map(int,input()))

n.sort(reverse=True)

for i in n:
    print(i, end='')
    
# 참고코드
# dict {} 및 lambda 함수 활용
'''
import sys
n = int(sys.stdin.readline())
so = []
for i in range(n):
    so.append(list(map(int, sys.stdin.readline().split())))
so.sort(key=lambda x: (x[0], x[1]))
for i in so:
    print(i[0], i[1])
'''