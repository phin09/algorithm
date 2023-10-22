# https://www.acmicpc.net/problem/11726
# 제출 전 문제 조건을 잘 읽자. 10007로 나눈 나머지를 출력하는 문제.
# 수의 크기가 커져서인지 __cache를 이용하는 게 더 빠름

# 방법 1
import sys

n = int(sys.stdin.readline())
dp = {1:1, 2:2}

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % 10007)

# 방법 2
# https://shoark7.github.io/programming/algorithm/%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9D%84-%ED%95%B4%EA%B2%B0%ED%95%98%EB%8A%94-5%EA%B0%80%EC%A7%80-%EB%B0%A9%EB%B2%95
import sys

def calcNumberOfCases(num, __cache = {1:1, 2:2}):
    if num in __cache:
        return __cache[num]

    __cache[num] = calcNumberOfCases(num-2) + calcNumberOfCases(num-1)
    return __cache[num]

n = int(sys.stdin.readline())
print(calcNumberOfCases(n) % 10007)