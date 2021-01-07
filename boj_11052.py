# https://www.acmicpc.net/problem/11052

# https://claude-u.tistory.com/279
# 참고 링크의 코드는 틀림

import sys

n = int(sys.stdin.readline())   # 구매하려고 하는 카드의 개수
price = [0] + list(map(int, sys.stdin.readline().split(' ')))

total = [0] * (n+1)
total[1] = price[1]
total[2] = max(price[2], total[1] + price[1])

for i in range(3, n+1):
    temp = total[1] + total[i - 1]
    for j in range(2, i//2 + 1):
        temp = max(temp, total[j] + total[i-j])
    total[i] = max(price[i], temp)

print(total[n])


# 참고할만한 다른 사람의 방법
# https://www.acmicpc.net/source/24918690