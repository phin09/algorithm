# https://www.acmicpc.net/problem/2442

import sys

n = int(sys.stdin.readline())

for i in range(1, n+1):
    print(f"{' ' * (n - i)}{'*' * ((2 * i) - 1)}")