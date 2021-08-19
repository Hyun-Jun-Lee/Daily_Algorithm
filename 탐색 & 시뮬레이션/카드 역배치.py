'''
▣ 입력설명총 10개의 줄에 걸쳐 한 줄에 하나씩 10개의 구간이 주어진다. i번째 줄에는 i번째 구간의 시작 위치 ai와 끝 위치 bi가 차례대로 주어진다. 
이때 두 값의 범위는 1 ≤ ai ≤ bi ≤ 20이다.

▣ 출력설명 1부터 20까지 오름차순으로 놓인 카드들에 대해, 
입력으로 주어진 10개의 구간 순서대로 뒤집는 작업을 했을 때 마지막 카드들의 배치를 한 줄에 출력한다.

▣ 입력예제 1
5 10
9 13
1 2
3 4
5 6
1 2
3 4
5 6
1 20
1 20

▣ 출력예제 1
1 2 3 4 10 9 8 7 13 12 11 5 6 14 15 16 17 18 19 20

'''

a = list(range(21)) # 0~20까지 자동 리스트 생성

for _ in range(10):
    s, e = map(int,input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i]

a.pop(0) # 0번째 인덱스 pop

for x in a:
    print(x, end='')