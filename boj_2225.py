# https://www.acmicpc.net/problem/2225

# https://it-garden.tistory.com/341
# 여기서 input lambda에 대해 알아볼 것
# 참고 링크의 코드에서 201을 n+1, k+1로 바꿨더니 런타임에러 남.

import sys

n, k = map(int, sys.stdin.readline().split(' '))
dp = [[0]*(201) for _ in range(201)]

for i in range(201):
    dp[1][i] = 1
    dp[2][i] = i + 1

for i in range(2, 201):
    dp[i][1] = i
    for j in range(2, 201):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j])

print(dp[k][n] % 1000000000)


# 런타임 에러
# import sys
#
# n, k = map(int, sys.stdin.readline().split(' '))
# dp = [[0]*(n+1) for _ in range(k+1)]
#
# for i in range(1, n+1):
#     dp[1][i] = 1
#     dp[2][i] = i + 1
#
# for i in range(2, k+1):
#     dp[i][1] = i
#     for j in range(2, n+1):
#         dp[i][j] = (dp[i][j-1] + dp[i-1][j])
#
# print(dp[k][n] % 1000000000)


# 참고할 다른 사람 풀이
# range에 n+1, k+1 넣고도 속도, 메모리 면에서 우수
# https://www.acmicpc.net/source/24621888


# 틀린 방법
# import sys
#
# n, k = map(int, sys.stdin.readline().split(' '))
# result = 0
#
# if n % k == 0:
#     result = (n // k) * k + 1
# elif n % k != 0:
#     result = ((n // k) + 1) * k
#
# print(result)