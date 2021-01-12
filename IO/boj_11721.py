# https://www.acmicpc.net/problem/11721

# 방법 1
import sys

inputStr = sys.stdin.readline()
for i in range(0, len(inputStr), 10):
    print(inputStr[i:i+10])

# 방법 2
import sys

temp = sys.stdin.readline()
for i in range(len(temp)//10):
    print(temp[i*10:i*10+10])
if len(temp)%10 != 0:
    print(temp[-(len(temp)%10):])