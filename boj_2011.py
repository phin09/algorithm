# https://www.acmicpc.net/problem/2011
# 반례 https://www.acmicpc.net/board/view/52607
# 반례 https://www.acmicpc.net/board/view/44917


# dp라 할 수 없는 방법...
import sys


def mul(num, __cache={1:1, 2:2, 3:3, 4:5}):
    if num in __cache:
        return __cache[num]
    __cache[num] = mul(num-2) + mul(num-1)
    return __cache[num]


def check(str):
    cases = 1
    cnt = 1
    for i in range(1, len(str)):
        if str[i] == '0':
            if str[i-1] == '1' or str[i-1] == '2':
                if cnt > 1:
                    cnt -= 1
                cases = cases * mul(cnt)
                cnt = 1
            else:
                return 0

        elif str[i] == '1' or str[i] == '2':
            if str[i-1] == '1' or str[i-1] == '2':
                cnt += 1

        elif str[i] == '7' or str[i] == '8' or str[i] == '9':
            if str[i-1] == '1':
                cnt += 1
                cases = cases * mul(cnt)
                cnt = 1
            elif str[i-1] == '2':
                cases = cases * mul(cnt)
                cnt = 1

        else:
            if str[i-1] == '1' or str[i-1] == '2':
                cnt += 1
                cases = cases * mul(cnt)
                cnt = 1

    return cases * mul(cnt)


inputStr = '0' + sys.stdin.readline().rstrip()
print(check(inputStr) % 1000000)


# 참고할 다른 사람 풀이
# https://www.acmicpc.net/source/24910007