# https://www.acmicpc.net/problem/9095

# 방법 1
import sys

t = int(sys.stdin.readline())   # 테스트 케이스 개수
dp = {1:1, 2:2, 3:4}
for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in range(t):
    print(dp[int(sys.stdin.readline())])

# 방법 2- 몇달 전의 내가 푼 거긴 한데 왜 이렇게 했던 건지..?
import sys

def calc(lst): # 중간과정값들을 list 받아 가능한 다음 중간과정값들을 list로 반환
    global count
    temp_lst = []
    for n in lst:
        if n == 0:
            count += 1 # 받아온 중간과정값 중 0이 있으면 방법 하나가 종료된 거니 count 하고 더이상 넘겨주지 않음
            continue # minus 값을 방지하기 위해 continue
        temp_lst.append(n - 1) # 1
        if n >= 2: # 2
            temp_lst.append(n - 2)
        if n >= 3: # 3
            temp_lst.append(n - 3)
    return temp_lst

T = int(sys.stdin.readline())
while(T > 0):
    n = int(sys.stdin.readline())
    flag = 0 # while loop 최초 시작 판별용
    count = 0

    while True:
        global result
        if n == 1:
            count = 1
            break
        if flag == 0: # 최초 시작
            temp = [n]
            flag = 1
        else:
            temp = result # 이전 loop의 중간과정값 받아옴
        result = [] # 중간과정값 받을 list 초기화
        result = calc(temp)
        if len(result) == 0: # result 전부 0이면 종료
            break

    print(count)
    T -= 1