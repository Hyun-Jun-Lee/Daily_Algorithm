'''
N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가 장 큰 합을 출력합 니다.

▣ 입력설명
첫 줄에 자연수 N이 주어진다.(1<=N<=50) 두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는 다.

▣ 출력설명 
최대합을 출력합니다.

▣ 입력예제 1

5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19

▣ 출력예제 1
155

'''

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)] 

for x in a:
    print(x)

largest = 0
for i in range(n):
    sum1 = sum2 = 0 # sum1:행의합, sum2:열의합
    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]

    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2

# 대각선의 합

sum1=sum2=0
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n-i-1]

if sum1 > largest:
    largest = sum1
if sum2 > largest:
    largest = sum2

print(largest)