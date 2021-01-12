# https://www.acmicpc.net/problem/1463

# 방법 1 - 재귀. 속도 빠름
# https://www.acmicpc.net/source/24706668
import sys

n = int(sys.stdin.readline())
dp = {1:0}

def cntCalc(num):
    if num in dp:   # dp에 있는 key인지 확인
        return dp[num]
    else:   # num보다 작은 key의 값이 필요하니 재귀
        if num % 2 == 0 and num % 3 == 0:
            dp[num] = min(cntCalc(num // 2) + 1, cntCalc(num // 3) + 1)
        elif num % 2 == 0:
            dp[num] = min(cntCalc(num - 1) + 1, cntCalc(num // 2) + 1)
        elif num % 3 == 0:
            dp[num] = min(cntCalc(num - 1) + 1, cntCalc(num // 3) + 1)
        else:
            dp[num] = cntCalc(num - 1) + 1

    return dp[num]

print(cntCalc(n))

# 방법 2 - 속도 빠름
import sys

def calc(lst): # 가능한 중간과정값들 다 내어보기
    temp_lst = []
    for n in lst:
        temp_lst.append(n - 1) # 받은 중간과정값에서 전부 다 1을 빼본 값 추가
        if n % 3 == 0:
            temp_lst.append(n / 3) # 받은 중간과정값에서 전부 다 3으로 나눠본 값 추가
        if n % 2 == 0:
            temp_lst.append(n / 2) # 받은 중간과정값에서 전부 다 2로 나눠본 값 추가
    temp_lst = list(set(temp_lst)) # 중복 제거
    return temp_lst

N = int(sys.stdin.readline())
count = 0
while True:
    if N == 1:
        break
    if count == 0: # 최초 시작
        temp = [N]
    else:
        temp = result # 이전 loop에서 가져온 중간과정값들을 temp에 넣음
    result = []  # 새로 중간과정값들 받을 리스트 초기화
    result = calc(temp) # 가능한 중간과정값들 다 받아오기
    count += 1
    if min(result) == 1:
        break
print(count)

# 방법 3 - 너무 느림
# https://velog.io/@khjcode/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-DP-%EB%AC%B8%EC%A0%9C-%ED%92%80%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC
import sys

n = int(sys.stdin.readline())
dp = [0, 0, 1]

for i in range(3, n+1):
    dp.append(dp[i-1] + 1) # 일단 1 작은 숫자의 연산 횟수 최솟값에다 1회를 더해 넣는다
    if i%2 == 0:   # 일단 넣어놨던 것과 //2를 하는 것 중 더 작은 걸로 바꾼다.
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i%3 == 0:   # 3도 마찬가지
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])


# 방법 4 - 너무 느림
# https://infinitt.tistory.com/247
import sys

n = int(sys.stdin.readline())
dp = [0 for _ in range(n+1)]    # dp[n]이 필요하니 n+1까지 자리 만들기

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1 # 일단 1 작은 숫자의 연산 횟수 최솟값에다 1회를 더해 넣는다
    if i%2 == 0 and dp[i] > dp[i//2] + 1:   # 일단 넣어놨던 것보다 //2를 하는 게 연산 횟수를 더 줄일 수 있다면 그걸 넣는다.
        dp[i] = dp[i//2] + 1
    if i%3 == 0 and dp[i] > dp[i//3] + 1:   # 3도 마찬가지
        dp[i] = dp[i//3] + 1

print(dp[n])

# 방법 5 - deque 이용
# https://www.acmicpc.net/source/24723384
from sys import stdin
from collections import deque

input = stdin.readline

N = int(input())
Q = deque([N])

arr = [False] * (10**6+1)
arr[N] = 1

while Q:
    tmp = Q.popleft()
    if tmp % 3 == 0 and arr[tmp//3] == False:
        arr[tmp//3] = arr[tmp] + 1
        Q.append(tmp//3)
    if tmp % 2 == 0 and arr[tmp//2] == False:
        arr[tmp//2] = arr[tmp] + 1
        Q.append(tmp//2)
    if arr[tmp-1] == False:
        arr[tmp-1] = arr[tmp] + 1
        Q.append(tmp-1)
    if arr[1]:
        break
print(arr[1]-1)