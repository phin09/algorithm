# https://www.acmicpc.net/problem/2522

# 방법 1
import sys

n = int(sys.stdin.readline())

for i in range(1, n+1):
    print(' ' * (n - i) + '*' * i)
for i in range(1, n):
    print(' ' * i + '*' * (n - i))

# 방법 2
import sys

N = int(sys.stdin.readline())
for i in range(1, N+1):
    print(' '*(N-i) + '*'*i)
for i in range(N-1, 0, -1):
    print(' '*(N-i) + '*'*i)