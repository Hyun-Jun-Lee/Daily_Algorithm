import sys

while True:
    m, n = map(int, sys.stdin.readline().split())
    if m == n == 0:
        break
    if n%m == 0:
        print('factor')
    elif m % n ==0:
        print('multiple')
    else:
        print('neither')
