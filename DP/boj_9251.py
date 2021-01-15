# https://www.acmicpc.net/problem/9251

import sys

s1 = sys.stdin.readline().rstrip()
s2 = sys.stdin.readline().rstrip()

dp = [[0] * (len(s1)+1) for _ in range(len(s2)+1)]


for i in range(1, len(s2)+1):
    for j in range(1, len(s1)+1):
        if s1[j-1] == s2[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])

# 같은 논리를 더 빠르게
# https://www.acmicpc.net/source/25144127
# a = input()
# b = input()
# n, m = len(a), len(b)
# dp = [[0] * m for _ in range(n)]
# dp[0][0] = int(a[0] == b[0])
# for i in range(1, m):
#     dp[0][i] = max(dp[0][i-1], int(a[0] == b[i]))
#
# for i in range(1, n):
#     dp[i][0] = max(dp[i-1][0], int(a[i] == b[0]))
#     for j in range(1, m):
#         if a[i] == b[j]:
#             dp[i][j] = 1 + dp[i-1][j-1]
#         else:
#             dp[i][j] = max(dp[i-1][j], dp[i][j-1])
#
# print(dp[-1][-1])