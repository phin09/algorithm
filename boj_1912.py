# https://www.acmicpc.net/problem/1912
# https://www.acmicpc.net/board/view/28134

# 방법 1
# https://claude-u.tistory.com/175
import sys

n = int(sys.stdin.readline())
inputArr = list(map(int, sys.stdin.readline().split(' ')))
temp = [0 for _ in range(n)]
maxVal = -1001

for i in range(n):
    temp[i] = max(temp[i-1]+inputArr[i], inputArr[i])
    maxVal = max(maxVal, temp[i])

print(maxVal)

# 방법 2
# https://www.acmicpc.net/source/24784874
n = int(input())
data = list(map(int, input().split()))
dp = [0]*n
dp[0] = data[0]

for i in range(1, n):
    dp[i] = max(data[i]+dp[i-1], data[i])

print(max(dp))


# 시간 초과 - O(n^2)
# import sys
#
# n = int(sys.stdin.readline())   # 수열의 원소 개수
# inputArr = list(map(int, sys.stdin.readline().split(' ')))
#
# def checkSum(num):
#     tempSum = inputArr[num]
#     tempArr = []
#     tempArr.append(tempSum)
#
#     for i in range(num+1, n):
#         tempSum += inputArr[i]
#         tempArr.append(tempSum)
#
#     return max(tempArr)
#
# sumArr = [checkSum(i) for i in range(n)]
# print(max(sumArr))