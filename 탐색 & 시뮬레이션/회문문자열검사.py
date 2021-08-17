'''
N개의 문자열 데이터를 입력받아 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우(회문 문자열) 이면 YES를 출력하고 회문 문자열이 아니면 NO를 출력하는 프로그램을 작성한다.
단 회문을 검사할 때 대소문자를 구분하지 않습니다.

▣ 입력설명첫 줄에 정수 N(1<=N<=20)이 주어지고, 그 다음 줄부터 N개의 단어가 입력된다.
각 단어의 길이는 100을 넘지 않는다.

▣ 출력설명각 줄에 해당 문자열의 결과를 YES 또는 NO로 출력한다.

▣ 입력예제 1
5
level 
moon 
abcba 
soon 
gooG

▣ 출력예제 1
#1 YES #2 NO #3 YES #4 NO #5 YES

'''

n = int(input())

# case1
for i in range(n):
    s = input()
    s = s.upper() # 모두 대문자화
    size = len(s)
    for j in range(size//2):
        if s[j] != s[-1-j]: #j번째 글자와 뒤에서 j번째 글자가 다르다면 no출력
            print("# %d NO" % (i+1)) # i가 0부터시작하니 +1
            break
    else:
        print("# %d Yes" % (i+1))

# case2

for i in range(n):
    s = input()
    s = s.upper() # 모두 대문자화
    if s==s[::-1]:
        print("# %d Yes" % (i+1))
    else:
        print("# %d NO" % (i+1))

        