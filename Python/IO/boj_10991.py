# https://www.acmicpc.net/problem/10991

import sys

n = int(sys.stdin.readline())

for i in range(1, n+1):
    print(' ' * (n - i) + '*' + ' *' * (i - 1))