# https://www.acmicpc.net/problem/9461

import sys

def padovan(num, __cache={1:1, 2:1, 3:1, 4:2, 5:2}):
    if num in __cache:
        return __cache[num]
    __cache[num] = padovan(num-1) + padovan(num-5)
    return __cache[num]

t = int(sys.stdin.readline())   # 테스트 케이스 개수

for _ in range(t):
    n = int(sys.stdin.readline())
    print(padovan(n))