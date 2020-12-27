# https://www.acmicpc.net/problem/2445

# 방법 1
import sys

n = int(sys.stdin.readline())

for i in range(1, n+1):
    print(f"{'*' * i}{' ' * 2*(n-i)}{'*' * i}")
for i in range(1, n):
    print(f"{'*' * (n - i)}{' ' * (2 * i)}{'*' * (n - i)}")

# 방법 2
import sys

N = int(sys.stdin.readline())
for i in range(1, N+1):
    print('*'*i + ' '*(2*(N-i)) + '*'*i)
for i in range(N-1, 0, -1):
    print('*'*i + ' '*(2*(N-i)) + '*'*i)