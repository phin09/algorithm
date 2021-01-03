# https://www.acmicpc.net/problem/10844

# https://pacific-ocean.tistory.com/151
import sys

n = int(sys.stdin.readline())
dp = [[0] * 10 for _ in range(n+1)]
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n]) % 1000000000)


# 실패한 방법
# import sys
#
# def calcStairNum(num, __cache={1:9}):
#     if num in __cache:
#         return __cache[num]
#     __cache[num] = (2 * calcStairNum(num-1) - (num - 1)) % 1000000000
#     return __cache[num]
#
# n = int(sys.stdin.readline())
# print(calcStairNum(n))