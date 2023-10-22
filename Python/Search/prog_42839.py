'''
https://programmers.co.kr/learn/courses/30/lessons/42839
완전탐색

permutations 함수 몰라서 풀이 검색함
https://eda-ai-lab.tistory.com/466
https://liveyourit.tistory.com/211

for문 돌릴 때 range 빼먹은 거 못 찾아서 고생함

set += set 해봤더니
TypeError: unsupported operand type(s) for +=: 'set' and 'set'
set |= set은 된다. https://python.bakyeono.net/chapter-9-2.html

set을 찍어보려니
TypeError: Object of type set is not JSON serializable

map, permutations, 소수 판별 공부하기
'''

from itertools import permutations
from math import sqrt

def solution(numbers):
    pool = []
    answer = 0
    
    for i in range(1, len(numbers)+1):
        temp = list(map(''.join, list(permutations(list(numbers), i))))
        for j in temp:
            pool.append(int(j))
            
    for k in list(set(pool)):
        if k < 2:
            continue
        
        flag = 1
        
        for denominator in range(2, int(sqrt(k))+1):
            if k % denominator == 0:
                flag = 0
        
        answer += flag
    
    return  answer