# https://www.acmicpc.net/problem/10869

# 방법 1
a, b = map(int, input().split(' '))
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)

# 방법 2
a, b = map(int, input().split(' '))
print('%d\n%d\n%d\n%d\n%d'%(a + b, a - b, a * b, a // b, a % b))