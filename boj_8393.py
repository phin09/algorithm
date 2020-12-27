# https://www.acmicpc.net/problem/8393

import sys

n = int(sys.stdin.readline())

result = sum([i for i in range(1, n + 1)])
print(result)