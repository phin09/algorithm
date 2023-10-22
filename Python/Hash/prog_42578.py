'''
https://programmers.co.kr/learn/courses/30/lessons/42578
'''

def solution(clothes):
    closet = {}
    answer = 1
    
    for item in clothes:
        if item[1] not in closet:
            closet[item[1]] = 1
        else:
            closet[item[1]] += 1
        
    for key, value in closet.items():
        answer = answer * (value + 1)
        
    return answer - 1