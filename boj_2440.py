# https://www.acmicpc.net/problem/2440

import sys

n = int(sys.stdin.readline())

for i in range(n, 0, -1):
    print('*' * i)