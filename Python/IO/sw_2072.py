# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QSEhaA5sDFAUq&categoryId=AV5QSEhaA5sDFAUq&categoryType=CODE
# 지금 풀이가 sw 표준 입출력 형식에 안 맞는 상태

import sys 

t = int(sys.stdin.readline())   # 테스트 케이스 개수

for i in range(t):
    result = 0
    arr = list(map(int, sys.stdin.readline().split(' ')))
    print(arr)
    for item in arr:
        if item % 2 == 1:
            result = result + item
    print(f'#{i+1} {result}')

# 결과:
# 제출 오류
# 파일 입력 메소드가 사용되었습니다.
# > sys.stdin
# (제출 코드에는 표준 입출력만 사용해야 합니다.)