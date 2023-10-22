# https://www.acmicpc.net/problem/2156

import sys

n = int(sys.stdin.readline())
wine = {}
for i in range(1, n+1):
    wine[i] = int(sys.stdin.readline())

dp = {1: wine[1]}
if n >= 2:
    dp[2] = wine[1] + wine[2]
if n >= 3:
    dp[3] = max(wine[1] + wine[3], wine[2] + wine[3], wine[1] + wine[2])

# 마지막 잔을 안 마실 때와 마실 때로 나눔
for i in range(4, n+1):
    dp[i] = max(dp[i-1], dp[i-3] + wine[i-1] + wine[i], dp[i-2] + wine[i])

print(dp[n])

# 공부해볼 다른 사람의 풀이
# https://www.acmicpc.net/source/24821123