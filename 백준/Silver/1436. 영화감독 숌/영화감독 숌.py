import sys

n = int(sys.stdin.readline())
num = 0
cnt = 0

# 브루트포스 문제는 1부터 하나씩 다돌아보기!
# num에 하나씩 더해가면서 해당 num에 '666'이 포함되면
# cnt에 1을 누적해줘서 '666'이 포함된 몇번째 숫자인지 파악
while True:
    if '666' in str(num):
        cnt += 1
    if cnt == n:
        print(num)
        break
    num += 1
