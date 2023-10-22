'''
https://programmers.co.kr/learn/courses/30/lessons/42584
stack으로 풂.
'''

# 세번째 풀이 - collections.deque
# 속도가 25% 이하 개선됨
from collections import deque

def solution(prices):
    answer = [0] * len(prices)
    stack = deque()
    
    for i in range(0, len(prices)-1):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    
    while stack:
        k = stack.pop()
        answer[k] = len(prices) - 1 - k
        
    return answer


# 두번째 풀이 - 첫번째 풀이 일부 수정
# def solution(prices):
#     answer = [0] * len(prices)
#     stack = []
    
#     for i in range(0, len(prices)-1):
#         while stack and prices[stack[-1]] > prices[i]:
#             answer[stack[-1]] = i - stack[-1]
#             stack.pop()
#         stack.append(i)
    
#     while stack:
#         answer[stack[-1]] = len(prices) -1 -stack[-1]
#         stack.pop()
        
#     return answer


# 첫번째 풀이
# def solution(prices):
#     answer = [0] * len(prices)
#     stack = []
    
#     for i in range(0, len(prices)-1):
#         while stack:
#             if prices[stack[-1]] > prices[i]:
#                 answer[stack[-1]] = i - stack[-1]
#                 stack.pop()
#             else:
#                 stack.append(i)
#                 break
#         stack.append(i)
    
#     while stack:
#         answer[stack[-1]] = len(prices) -1 -stack[-1]
#         stack.pop()
        
#     return answer