'''
https://programmers.co.kr/learn/courses/30/lessons/42577

sort는 원본 변경, sorted는 사본 생성임을 기억하기.
'''

def solution(phone_book):
    phone_book.sort(key=len, reverse=True)
    hashed_phone = {}
    answer = True
    
    for phone in phone_book:
        temp_lst = [phone[:i] for i in range(1, len(phone)+1)]
        if phone in hashed_phone:
            answer = False
            break;
        else:
            for sliced_phone in temp_lst:
                hashed_phone[sliced_phone] = 1
                
    return answer


'''
효율성 탈락인 코드

import re

def solution(phone_book):
    phone_book.sort()
    book = {}
    len_num = {}
    answer = True
    
    for i in range(len(phone_book)):
        book[phone_book[i]] = len(phone_book[i])
    
    for i in range(len(phone_book)):
        p = re.compile(phone_book[i])
        for j in range(i+1, len(phone_book)):
            m = p.match(phone_book[j])
            if m != None:
                answer = False
    
    return answer
'''