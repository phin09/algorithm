# https://www.acmicpc.net/problem/11057

# 방법 1
import sys
sys.setrecursionlimit(10000)

def calc(num, __cache = {1:[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}):
    if num in __cache:
        return __cache[num]
    __cache[num] = []
    for i in range(1, 11):
        __cache[num].append(sum([calc(num-1)[j-1] for j in range(1, i+1)]))
    return __cache[num]

n = int(sys.stdin.readline())
print(sum(calc(n)) % 10007)


# 공부해볼 다른 사람의 풀이
# https://www.acmicpc.net/source/24701498