# https://www.acmicpc.net/problem/2193

# 방법 1
import sys

n = int(sys.stdin.readline())
dp = {1:1, 2:1}

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])

# 방법 2
# https://shoark7.github.io/programming/algorithm/%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9D%84-%ED%95%B4%EA%B2%B0%ED%95%98%EB%8A%94-5%EA%B0%80%EC%A7%80-%EB%B0%A9%EB%B2%95
# 파이썬 함수의 동작 방식을 활용. __cache를 함수 내부가 아닌 정의부에 선언해 함수 호출, 종료와 상관 없이 함수 자체가 지워지기 전까지 유지된다.
import sys

def fibo(N, __cache={0: 0, 1: 1, 2: 1}):
    if N in __cache:
        return __cache[N]

    __cache[N] = fibo(N - 1) + fibo(N - 2)
    return __cache[N]

N = int(sys.stdin.readline())
print(fibo(N))