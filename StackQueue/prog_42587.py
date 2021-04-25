'''
https://programmers.co.kr/learn/courses/30/lessons/42587
queue
'''

from collections import deque

def solution(priorities, location):
    queue = deque()
    answer = 0
    
    for i in range(len(priorities)):
        target =  1 if i == location else 0
        queue.append((priorities[i], target))
    
    priorities.sort()
    
    i = 1
    while queue:
        if queue[0][0] == priorities[-1]:
            if queue.popleft()[1] == 1:
                return i
            i += 1
            priorities.pop()
        else:
            queue.append(queue.popleft())