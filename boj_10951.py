# https://www.acmicpc.net/problem/10951

# 방법 1
inputStr = input()

while True:
    a, b = map(int, inputStr.split(' '))
    print(a + b)
    try:
        inputStr = input()
    except:
        break

# 방법 2
import sys

while True:
    try:
        a, b = map(int, sys.stdin.readline().split(' '))
        print(a + b)
    except:
        break