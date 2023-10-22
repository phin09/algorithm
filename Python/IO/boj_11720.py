# https://www.acmicpc.net/problem/11720

# 방법 1
import sys

n = int(input())
inputStr = sys.stdin.readline()
result = 0

for i in range(n):
    result = result + int(inputStr[i])

print(result)

# 방법 2
# 1차원 list는 sum(list)로도 총합을 구할 수 있다.
import sys

n = int(sys.stdin.readline())
inputStr = sys.stdin.readline()
result = sum([int(inputStr[i]) for i in range(n)])
print(result)