# input : int
# 숫자 num을 입력받고 뒤집은 모양이 num과 같은지 여부를 반환
# output : boolean

# 삼항연산자(Ternary Operator) 사용
def same_reverse(num):
    return 1 if str(num) == str(num)[::-1] else 0

# 풀어쓴 게 아래
def same_reverse(num):
    str_num = str(num)
    if str_num == str_num[::-1]:
        return True
    return False
