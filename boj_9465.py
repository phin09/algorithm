# https://www.acmicpc.net/problem/9465

# https://suri78.tistory.com/94
# 방법 1에서 시간을 더 줄일 수 있는 방법
# 참고링크처럼 dp를 따로 선언하지 않고 입력배열에 더해나가기
# 또는 함수화하기

# 틀린 코드
# dp = [([0] * n) * 2]
# print(dp)   # [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
# 해결: dp = [[0] * n for _ in range(2)] 또는 dp = [[0] * n] * 2

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    matrix = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(2)]
    dp = [[0] * n for _ in range(2)]

    dp[0][0] = matrix[0][0]
    dp[1][0] = matrix[1][0]
    dp[0][1] = matrix[0][1] + dp[1][0]
    dp[1][1] = matrix[1][1] + dp[0][0]

    for i in range(2, n):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + matrix[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + matrix[1][i]

    print(max(dp[0][n-1], dp[1][n-1]))