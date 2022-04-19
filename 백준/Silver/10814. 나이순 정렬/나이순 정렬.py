import sys

n = int(sys.stdin.readline())
users = []
for _ in range(n):
    users.append(sys.stdin.readline().split())

users.sort(key= lambda x:int(x[0]))

for i in users:
    print(i[0],i[1])