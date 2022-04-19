n = int(input())
num = []
for _ in range(n):
    a,b = map(int,input().split())
    num.append((b,a))

num.sort()

for i in range(n):
    print(num[i][1], num[i][0] )