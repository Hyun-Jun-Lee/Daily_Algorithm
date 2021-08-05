'''
N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력
하는 프로그램을 작성하세요. 각 자연수의 자릿수의 합을 구하는 함수를 def digit_sum(x)를
꼭 작성해서 프로그래밍 하세요.

▣ 입력설명
첫 줄에 자연수의 개수 N(3<=N<=100)이 주어지고, 그 다음 줄에 N개의 자연수가 주어진다.
각 자연수의 크기는 10,000,000를 넘지 않는다.

▣ 출력설명
자릿수의 합이 최대인 자연수를 출력한다. 자릿수의 합이 같을 경우 입력순으로 먼저인 숫자
를 출력합니다.

▣ 입력예제 1
3
125 15232 97

▣ 출력예제 1
97

'''

n = int(input())
a = list(map(int, input().split()))

def digit_sum(x):
    sum = 0 #각 자릿수 더할 값
    while x>0: # False가 될 때까지(x<=0) 반복
        sum += x%10 #나머지 + ex) 125 % 10= 5가 sum에 누적 -> 12%10=2가 sum에 누적 -> 2%10=1가 sum에 누적
        x=x//10 # 몫 ex)125//10 = 12 , x= 12 -> 12//10=2, x=2 -> 2//10=0, x=0 break
    return sum

'''
# case 2

def digit_sum(x):
    sum=0
    for i in str(x): #x를 문자열 처리해서 한글자씩 접근
        sum += int(i) # i를 문자->숫자
    return sum

'''

max = 0
for x in a:
    total=digit_sum(x)
    if total>max:
        max=total
        res=x
print(res)

