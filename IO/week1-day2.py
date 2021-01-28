# input : int
# 입력받은 숫자를 뒤집어서 반환한다. 결과값이 유효한 정수가 되도록 0과 - 기호의 위치를 고려하기.
# output : int

# 재이님 코드 참고
def reverse(number):
    str_num = str(number)[::-1]
    if str_num[-1] == '-':
        return int('-' + str_num[:-1])
    return int(str_num)


# 최초 풀이 - not pythonic
# iterable과 아닌 type간 변환에 대한 직관 부족
# pop이 뒤에서부터 뽑는지 앞에서부터 뽑는지 확신이 없음
# lst.reverse() 이 코드 째로 변수에 할당하면 안 된다는 걸 몰랐음
# flag는 군더더기임.
# while 부분의 0 처리도 군더더기임. 어차피 int 변환하면 유효한 int가 되면서 앞쪽의 0이 날아감.

# def reverse(number):
  # number_lst = list(str(number))

  # flag = 0
  # if number == 0:
  #   return 0
  # elif number < 0:
  #   flag = -1
  #   number_lst.pop(0)
  
  # while True:
  #   if number_lst[-1] == 0:
  #     number_lst.pop()
  #   else:
  #     break

  # number_lst.reverse()

  # new_number = int(''.join(number_lst))

  # if flag == -1:
  #   return 0 - new_number
  # return new_number

