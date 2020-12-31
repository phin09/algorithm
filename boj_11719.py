# https://www.acmicpc.net/problem/11719

import sys
print(sys.stdin.read())

# 결과는 같은데 출력 초과
# 이유 참고: https://www.acmicpc.net/board/view/28332
import sys

while(True):
    try:
        print(sys.stdin.readline().strip())
    except:
        break