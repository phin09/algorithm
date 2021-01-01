# https://www.acmicpc.net/problem/11055
# boj 11053과 같은 유형

# 지금 찝은 원소 기준 좌측에서 보다 작은 값인 동시에 증가 부분 수열의 합이 큰 걸 찾기.
# 합을 저장한 배열에서 가장 큰 값을 return
import sys

n = int(sys.stdin.readline())
inputArr = list(map(int, sys.stdin.readline().split(' ')))

sumArr = [0 for _ in range(n)]  # 증가 부분 수열의 합
sumArr[0] = inputArr[0]    # index가 0일 때 자기 자신을 합으로 넣어둠
# 이게 없으면 이 원소가 들어가는 모든 합에서 이 값이 빠진 상태로 나옴

for i in range(1, n):   # 내부 for문을 실행하기 위해 1부터 시작
    tempMax = 0
    for j in range(i):
        if inputArr[j] < inputArr[i] and sumArr[j] >= tempMax:
            tempMax = sumArr[j]
    sumArr[i] = tempMax + inputArr[i]

print(max(sumArr))
