# https://www.acmicpc.net/problem/10952

# 방법 1
while(True):
    a, b = map(int, input().split(' '))
    if a == 0 & b == 0:
        break
    print(a + b)
    
# 방법 2
import sys

while True:
    a, b = map(int, sys.stdin.readline().split(' '))
    if a == 0 and b == 0:
        break
    else:
        print(a + b)