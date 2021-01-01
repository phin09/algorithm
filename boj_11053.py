# https://www.acmicpc.net/problem/11053

# 방법 1
# 지금 찝은 원소의 좌측에서 보다 작은 값이 있는지 찾고, 그 작은 값이 갖고 있는 증가 수열의 최대값을 가져옴.
# 좌측의 원소를 다 검사해서 그 중 유효하면서 가장 긴 증가 수열의 길이를 가져오고, +1을 해서 지금 찝은 원소를 끝으로 하는 증가 수열의 최대 길이를 저장한다.
# 증가 수열의 최대 길이만 저장해둔 tempArr에서 가장 큰 값을 정답으로 return한다.
import sys

n = int(sys.stdin.readline())
inputArr = list(map(int, sys.stdin.readline().split(' ')))

tempArr = [1 for _ in range(n+1)]  # 수열 원소의 최소값 1
# 해당 index의 inputArr값이 갖는 증가 수열의 최대 길이를 저장

for i in range(1, n):   # 내부 for문을 실행하기 위해 1부터 시작
    tempMax = 0
    for j in range(i):
        if inputArr[j] < inputArr[i] and tempArr[j] > tempMax:
            tempMax = tempArr[j]
    tempArr[i] = tempMax + 1    # 자신(inputArr[i])도 포함한 길이로 증가수열의 최대 길이를 넣어줌

print(max(tempArr))

# 방법 2
# https://suri78.tistory.com/m/96?category=807697
# A에 들어가는 수의 범위가 클 때에는 쓰기 어려워보임.
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split(' ')))

lst = [0] * 1001 # 수가 1~1000 사이이기 때문
for i in A:
    lst[i] = max(lst[:i]) + 1 # +1 넣어서 자기 자신 포함
    # 값 i를 받았을 때 i보다, 작은 범위 내에서 가장 큰 값에 들어가 있는 값을 가져옴.
    # A가 [10, 20, 10, 30]일 때
    # i = 10 들어가면 index가 10보다 작은 범위에서는 다 0이니 lst[10] = 1
    # i = 20 들어가면 20보다 작은 범위에서 가장 큰 값은 lst[10] = 1이므로 lst[20] = 2
    # 이는 10 -> 20 으로 증가하는 부분순열이 만들어진다는 뜻.
    # i = 10 들어가면 index가 10보다 작은 범위에서는 다 0이니 lst[10] = 1
    # i = 30 들어가면 30보다 작은 범위에서 가장 큰 값은 lst[20] = 2이므로 lst[30] = 3
    # 가장 긴 증가하는 부분순열 [10, 20, 30] 길이 3.

print(max(lst))

# 방법 3 - 이분탐색. 시간 짧고 사용하는 메모리가 크다
# https://www.acmicpc.net/source/24788970