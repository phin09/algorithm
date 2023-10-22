'''
https://programmers.co.kr/learn/courses/30/lessons/42842
완전탐색

'''

def solution(brown, yellow):
    width_plus_height = brown//2 + 2
    for h in range(2, width_plus_height//2+1):
        w = width_plus_height - h
        if (h-2) * (w-2) == yellow:
            answer = [w, h]
            break
    
    return answer