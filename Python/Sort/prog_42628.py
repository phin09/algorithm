'''
https://programmers.co.kr/learn/courses/30/lessons/42628
heapq
참고 https://www.daleseo.com/python-heapq/
'''

import heapq

def solution(operations):
    target = []
    cnt = 0
    for operation in operations:
        if 'I' in operation:
            heapq.heappush(target, int(operation[2:]))
        elif '-' in operation and target:
            heapq.heappop(target)
        elif target:
            target.sort()
            target = target[:-1]

    target.sort(reverse=True)
    if target:
        answer = [target[cnt], target[-1]]
    else:
        answer = [0, 0]
        
    return answer