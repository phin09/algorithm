# https://www.acmicpc.net/problem/10818

# 방법 1
import sys

n = int(sys.stdin.readline())
inputArr = list(map(int, sys.stdin.readline().split(' ')))
maxInput = inputArr[0]
minInput = inputArr[0]

for i in range(n):
    if inputArr[i] > maxInput:
        maxInput = inputArr[i]
    elif inputArr[i] < minInput:
        minInput = inputArr[i]

print(minInput, maxInput)

# 방법 2
import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split(' ')))
lst.sort()
print(f"{lst[0]} {lst[-1]}")
