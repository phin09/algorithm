# https://www.acmicpc.net/problem/2331

import sys


def calcNew(n):
    temp = 0
    for i in range(len(str(numbers[n-1]))):
        temp += int(str(numbers[n - 1])[i:i + 1]) ** p
    return temp


a, p = map(int, sys.stdin.readline().split(' '))
n = 0
numbers = []
numbers.append( a)
loopStartsAt = 0

while True:
    n += 1
    tempNum = calcNew(n)
    if tempNum in numbers:
        loopStartsAt = numbers.index(tempNum)
        break
    else:
        numbers.append(tempNum)

print(loopStartsAt)