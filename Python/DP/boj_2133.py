# https://www.acmicpc.net/problem/2133
# https://algorithmist.com/wiki/UVa_10918_-_Tri_Tiling
# https://blog.naver.com/hands731/221806277981
# https://blog.naver.com/cldlakd/221411915772
import sys

def calcNumberOfCases(num, __cache = {0:1, 2:3}):
    if num % 2 == 1:
        return 0
    if num in __cache:
        return __cache[num]

    tempSum = 0
    for i in range(4, num-1, 2):
        tempSum += 2 * calcNumberOfCases(num-i)
    __cache[num] = __cache[2] * calcNumberOfCases(num-2) + tempSum + 2

    return __cache[num]

n = int(sys.stdin.readline())
print(calcNumberOfCases(n))

# 이중 for문에 주는 값을 바꿔서 표현한 다른 사람의 풀이
# https://www.acmicpc.net/source/24386828