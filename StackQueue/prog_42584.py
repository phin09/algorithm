'''
https://programmers.co.kr/learn/courses/30/lessons/42584
stack으로 풂.

collections.deque로 풀어보기
'''

def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    for i in range(0, len(prices)-1):
        while stack:
            if prices[stack[-1]] > prices[i]:
                answer[stack[-1]] = i - stack[-1]
                stack.pop()
            else:
                stack.append(i)
                break
        stack.append(i)
    
    while stack:
        answer[stack[-1]] = len(prices) -1 -stack[-1]
        stack.pop()
        
    return answer