# https://www.acmicpc.net/problem/1699

# 방법 1 - 속도 엄청 느림
# https://pacific-ocean.tistory.com/205
import sys

n = int(sys.stdin.readline())
dp = [0] * (n+1)
square = [i*i for i in range(1, 317)]
for i in range(1, n+1):
    tempArr = []
    for j in square:
        if j > i:
            break
        tempArr.append(dp[i-j])
    dp[i] = min(tempArr) + 1
print(dp[n])

# 방법 2 - 속도 빠름
# https://www.acmicpc.net/source/24558529
memo = {0: 0, 1: 1}

def routine(n):
    if n in memo:
        return memo[n]

    near_square_root = int(n ** 0.5)
    near_square = near_square_root ** 2
    remainder = n - near_square

    if remainder == 0:
        memo[n] = 1
        return 1

    min_cnt = routine(near_square) + routine(remainder)
    start = near_square_root - 1
    end = int((n // 2) ** 0.5) - 1

    for square_root in range(start, end, -1):
        remainder = n - square_root ** 2
        cnt = routine(square_root ** 2) + routine(remainder)
        if cnt < min_cnt:
            min_cnt = cnt

    memo[n] = min_cnt
    return min_cnt

n = int(input())
print(routine(n))


# 런타임 에러
# import sys
# from math import sqrt, floor
# sys.setrecursionlimit(10000)
#
# def findSquare(num, __cache={0:0, 1:1}):
#     if num in __cache:
#         return __cache[num]
#     tempNum = floor(sqrt(num))
#     tempArr = []
#     for i in range(1, tempNum+1):
#         tempArr.append(findSquare(num-i**2))
#     __cache[num] = min(tempArr) + 1
#     return __cache[num]
#
# n = int(sys.stdin.readline())
# print(findSquare(n))