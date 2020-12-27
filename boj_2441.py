# https://www.acmicpc.net/problem/2441

import sys

n = int(sys.stdin.readline())

for i in range(n):
    print(f"{' ' * i}{'*' * (n-i)}")