# input : int
# 하나의 함수만 선언하여 재귀로 팩토리얼 결과 구하기
# output : input의 팩토리얼 결과값 int

# 문제에서 주어진 함수 선언 def factorial(n)에 맞추어 선언시 cache 딕셔너리를 넣는 방법은 쓰지 않았다.
def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1) * n
