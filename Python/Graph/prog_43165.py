'''
https://programmers.co.kr/learn/courses/30/lessons/43165
BFS, 비트연산

'''

# BFS

from collections import deque

def solution(numbers, target):
    queue = deque([ [numbers[0], 0], [-numbers[0], 0] ])
    idx_n = len(numbers)
    answer = 0
    
    while queue:
        num, idx = queue.popleft()
        idx += 1
        if idx == idx_n and num == target:
            answer += 1
        elif idx < idx_n:
            queue.append([num+numbers[idx], idx])
            queue.append([num-numbers[idx], idx])
            
    return answer


# 완전탐색

# def solution(numbers, target):
#     curr = [0]
#     for i in numbers:
#         temp = []
#         for j in curr:
#             temp += [j+i, j-i]
#         curr = temp

#     answer = 0        
#     for k in curr:
#         if k == target:
#             answer += 1
#     return answer


# 예전 풀이 - 비트연산 이용

def solution(numbers, target):
    answer = 0
    for i in range(2**len(numbers)): # 전체 경우의 수 2^n가지
        temp = []
        for j in range(len(numbers)):
            # 비트연산 이용
            if i & (2**j) == 0: 
                temp.append(numbers[j])
            else:
                temp.append(-1*numbers[j])
            """ else로 넘어간 (i. j)
            0 - 1가지: (0, -)
            1 - 5가지: (1, 0), (2, 1), (4, 3), (8, 3), (16, 4)
            2 - 10가지: (3, 0), (3, 1), (5, 0), (5, 2), (6, 1), (6, 2), (9, 0), (9, 3), (10, 1), (10, 3), (12, 2), (12, 3), 
                (17, 0), (17, 4), (18, 1), (18, 4), (20, 2), (20, 4), (24, 3), (24, 4)
            3 - 10가지: (7, 0), (7, 1), (7, 2), (11, 0), (11, 1), (11, 3), (13, 0), (13, 2), (13, 3), (14, 1), (14, 2), (14, 3),
                (19, 0), (19, 1), (19, 4), (21, 0), (21, 2), (21, 4), (22, 1), (22, 2), (22, 4), (25, 0), (25, 3), (25, 4),
                (26, 1), (26, 3), (26, 4), (28, 2), (28, 3), (28, 4)
            4 - 5가지: (15, 0), (15, 1), (15, 2), (15, 3), (23, 0), (23, 1), (23, 2), (23, 4)
                (27, 0), (27, 1), (27, 3), (27, 4), (29, 0), (29, 2), (29, 3), (29, 4)
                (30, 1), (30, 2), (30, 3), (30, 4)
            5 - 1가지: (31, 0), (31, 1), (31, 2), (31, 3), (31, 4)"""
                
        if sum(temp) == target:
            answer += 1        
    return answer