# https://www.acmicpc.net/problem/26041

# 방법 1
import sys

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()

lst = a.split()
bLength = len(b)
answer = 0

for item in lst:
    # B와 같은 길이면 B를 접두사로 가지는 동시에 B와 다를 수 없음
    if (len(item) == bLength):
        continue

    # B를 접두사로 갖는지 확인
    if (item[0:bLength] != b):
        continue

    answer += 1

print(answer)


# 방법 2 - 방법 1보다 조금 빠르게 (하지만 가독성 하락)
import sys

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()

lst = a.split()
bLength = len(b)
answer = 0

for item in lst:
    # B를 접두사로 갖는지 확인
    if (item[:bLength] != b):
        continue

    # B와 같지 않은지 확인
    answer = answer + 1 if item != b else answer

print(answer)


# 배운 것
# 대괄호 안에 for문, if문을 넣을 수 있다

# https://www.acmicpc.net/source/68461687
print(len([aa for aa in a if aa[:len(b)] == b and aa != b]))



