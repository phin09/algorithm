# https://www.acmicpc.net/problem/11022

import sys

t = int(input())

for i in range(t):
    a, b = map(int, sys.stdin.readline().split(' '))
    print(f'Case #{i + 1}: {a} + {b} = {a + b}')