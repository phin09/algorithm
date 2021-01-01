# https://www.acmicpc.net/problem/11727

# 방법 1
import sys

def calcNumberOfCases(num, __cache = {1:1, 2:3}):
    if num in __cache:
        return __cache[num]
    __cache[num] = 2 * calcNumberOfCases(num-2) + calcNumberOfCases(num-1)
    return __cache[num]

n = int(sys.stdin.readline())
print(calcNumberOfCases(n) % 10007)

# 방법 2 - 예전에 내가 푼 거
import sys

def tile(N, __cache = {1:1, 2:3}):
    if N in __cache:
        return __cache[N]
    if N % 2 == 0:
        temp = 1
    else:
        temp = -1

    __cache[N] = 2 * tile(N-1) + temp # N이 짝수면 +1, 홀수면 -1
    return __cache[N]

n = int(sys.stdin.readline())
print(tile(n) % 10007)
