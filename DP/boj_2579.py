# https://www.acmicpc.net/problem/2579

# https://infinitt.tistory.com/255
# dict 써서 풀 때는 keyError 주의.
# 런타임 에러의 원인을 못 찾다가 https://www.acmicpc.net/board/view/52258 이걸 보고 찾음.
import sys

n = int(sys.stdin.readline())
stairs = {}
for i in range(1, n+1):
    stairs[i] = int(sys.stdin.readline())

dp = {}
dp[1] = stairs[1]
if n >= 2:
    dp[2] = stairs[1] + stairs[2]
if n >= 3:
    dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

for i in range(4, n+1):
    dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i])

print(dp[n])

# 공부해볼 다른 사람의 풀이
# https://www.acmicpc.net/source/24820515