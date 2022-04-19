import sys

n = int(sys.stdin.readline())
alpha = []
for _ in range(n):
    # sys.stdin.readline()은 '\n\'을 포함하는 입력
    # strip()로 해결
    alpha.append(sys.stdin.readline().strip())

# 중복 없애기 위해 set(), sort 사용하기위해 list로 다시 변경
alpha = list(set(alpha))
alpha.sort()
# lambda 함수로 key 지정
alpha.sort(key= lambda x:len(x))

for i in alpha:
    print(i)
    