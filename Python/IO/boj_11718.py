# https://www.acmicpc.net/problem/11718

# 방법 1
while(True):
    try:
        print(input())
    except:
        break

# 방법 2
import sys
print(sys.stdin.read())

# 테스트 결과는 같은데 출력 초과
# import sys
#
# while(True):
#     try:
#         inputStr = sys.stdin.readline().strip()
#         print(inputStr)
#     except:
#         break
