# https://www.acmicpc.net/problem/2588

# 방법 1
a = int(input())
b = input()
print(a * int(b[2]))
print(a * int(b[1]))
print(a * int(b[0]))
print(a * int(b))

# 방법 2
a = int(input())
b = int(input())

print(a * (b % 10))
print(a * (b // 10 % 10))
print(a * (b // 100))
print(a * b)