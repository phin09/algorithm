# https://www.acmicpc.net/problem/11054
# boj 11053과 같은 유형

import sys
from operator import add

n = int(sys.stdin.readline())
inputArr = list(map(int, sys.stdin.readline().split(' ')))
ascArr = [1 for _ in range(n)]  # 증가 수열의 길이를 저장할 배열
descArr = [1 for _ in range(n)] # 감소 수열의 길이를 저장할 배열

# 증가 수열
for i in range(1, n):
    tempMax = 0
    for j in range(i):
        if inputArr[j] < inputArr[i] and ascArr[j] > tempMax:
            tempMax = ascArr[j]
    ascArr[i] = tempMax + 1 # 자신(inputArr[i])도 포함하기 위해 +1

# 감소 수열
for i in range(n-1, -1, -1):    # 오른쪽에서 왼쪽으로 가면서 기준의 우측을 확인
    tempMax = 0
    for j in range(i+1, n):
        if inputArr[j] < inputArr[i] and descArr[j] > tempMax:
            tempMax = descArr[j]
    descArr[i] = tempMax + 1

#print(ascArr)
#print(descArr)
result = list(map(add, ascArr, descArr))
# print(result)
print((max(result)) - 1)
# 기준(가장 큰 수)이 중복으로 더해졌으니 -1