# https://www.acmicpc.net/problem/10953

import sys

t = int(input())

for i in range(t):
    a, b = map(int, sys.stdin.readline().split(','))
    print(a + b)
