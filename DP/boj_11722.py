# https://www.acmicpc.net/problem/11722
# boj 11053과 같은 유형

import sys

n = int(sys.stdin.readline())
inputArr = list(map(int, sys.stdin.readline().split(' ')))
tempArr = [1] * n

for i in range(n-1, -1, -1):
    tempMax = 0
    for j in range(i+1, n):
        if inputArr[j] < inputArr[i] and tempArr[j] > tempMax:
            tempMax = tempArr[j]
    tempArr[i] = tempMax + 1

print(max(tempArr))