# https://programmers.co.kr/learn/courses/4008
# 파이썬을 파이썬답게

# 이중배열 각 요소의 배열 길이를 return하는 문제에서
def solution(mylist):
    answer = []
    for i in mylist:
        answer.append(len(i))
    return answer

# 위는 C, Java스러운 풀이. 아래가 파이썬 방식
def soultion(mylist):
    return list(map(len, mylist))

# 몫과 나머지 구하기
# divmod: Return the tuple (x//y, x%y)
# *는 unpacking
a = 7
b = 5
print(*divmod(a, b))

# unpacking
lst = [1, 2, 3]
print(*lst) # 1 2 3
print(lst) # [1, 2, 3]

# n진수 수를 10진수로 변환
# int(x, base) -> base(int)진수의 x(str)라는 숫자를 10진수로 변환
num, base = map(str, input().strip().split(' '))
print(int(num, int(base)))

# 문자열을 좌측, 가운데, 우측 정렬하기
# f-string 응용 또는 string의 method 사용
# print(f'{}')에서 {}를 이중으로 써도 된다는 것도 확인함.
s, n = input().strip().split(' ')
n = int(n)
print(f'{s:<{n}}')  # s.ljust(n)
print(f'{s:^{n}}')  # s.center(n)
print(f'{s:>{n}}')  # s.rjust(n)

# string constant
import string

string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters #대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 숫자 0123456789

# 원본을 유지한 채 정렬하기
# copy.deepcopy하고 sort하거나
# sorted
list1 = [3, 2, 1]
list2 = sorted(list1)

# copy.deepcopy
list1 = [3, 2, 1]
list2 = [i for i in list1]

# 2차원 배열의 열과 행을 뒤집기
mylist = [ [1,2,3], [4,5,6], [7,8,9] ]
new_list = list(map(list, zip(*mylist)))

# 리스트 내 모든 요소의 type 변경
# 부동소숫점 튜플 (3.14, 3.5, 22.6)을 정수 배열 (3, 3, 22)로 바꾸기
# 문자열 배열 ['1', '100', '33']을 정수 배열 [1, 100, 33]로 바꾸기
list1 = ['1', '100', '33']
list2 = list(map(int, list1))

# 각 원소의 길이를 담은 리스트를 리턴
# input [[1], [2]]
# output [1,1]
def solution(mylist):
    answer = list(map(len, mylist))
    return answer

# 배열의 모든 요소를 이어붙인 문자열을 리턴
# 문자열 배열뿐만 아니라 정수형 튜플에서도 이용 가능 -> 정수형 튜플에서 되는거 맞음???
my_list = ['1', '100', '33']
answer = ''.join(my_list)   # "110033"

# * 이용해서 반복
# 문자열뿐만 아니라 배열에도 사용 가능
answer= [123, 456]*3
print(answer)   # [123, 456, 123, 456, 123, 456]

# 곱집합
import itertools

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'
itertools.product(iterable1, iterable2, iterable3)

# 2차원 리스트를 1차원 리스트로 만들기

# 별로인 방법 1
my_list = [[1, 2], [3, 4], [5, 6]]
answer = []
for items in mylist:
    for item in items:
        answer.append(item)
# 별로인 방법 2
answer = []
for i in my_list:
    answer += i

# 방법 1 - sum 함수
answer = sum(my_list, [])

# 방법 2 - itertools.chain
import itertools
list(itertools.chain.from_iterable(my_list))

# 방법 3 - itertools와 unpacking
import itertools
list(itertools.chain(*my_list))

# 방법4 - list comprehension 이용
[element for array in my_list for element in array]

# 방법 5 - reduce 함수 이용1
from functools import reduce
list(reduce(lambda x, y: x+y, my_list))

# 방법 6 - reduce 함수 이용2
from functools import reduce
import operator
list(reduce(operator.add, my_list))

# 방법 7 - numpy 라이브러리의 flatten 이용
import numpy as np
np.array(my_list).flatten().tolist()

# 순열, 조합
def permute(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result
# 파이썬에서는 아래처럼 가능
# 조합은 itertools.combinations
import itertools

pool = ['A', 'B', 'C']
print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 만들기

# str요소 list를 입력값으로 하고 map에 ''.join 쓰면
# ["12","21"]
# 숫자요소 list를 입력값으로 하고 map에 str 쓰면 에러남
# str 요소 list를 입력값으로 하고 map에 str 쓰면
# ["('1', '2')","('2', '1')"]
# str 요소 list를 입력값으로 하고 map에 list 쓰면
# [["1","2"],["2","1"]]
# 숫자요소 list를 입력값으로 하고 map에 list 쓰면
# [[1, 2], [2, 1]]

# 내가 푼 코드
import itertools

def solution(mylist):
    mylist.sort()   # 순열이 사전순이 되기 위해 먼저 정렬함
    answer = list(map(list, itertools.permutations(mylist)))
    return answer

# 가장 많이 등장하는 알파벳 찾기
# collections.Counter
# 리스트를 넣으면 리스트의 원소가 key로, cnt가 value로 들어가는 dict를 만들어줌
# 내가 푼 코드. 질문게시판에서 다른 사람것도 보기(lambda 함수쓰는거 공부해야될듯..)
from collections import Counter

my_str = input().strip()
tempArr = []
for i in range(len(my_str)):
    key = my_str[i:i+1]
    tempArr.append(key)
    
tempDict = Counter(tempArr)
maxCnt = max(tempDict.values())
result = []
for key, value in tempDict.items():
    if value == maxCnt:
        result.append(key)

result.sort()
print(''.join(result))

