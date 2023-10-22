'''
https://programmers.co.kr/learn/courses/30/lessons/42583
queue
'''

from collections import deque

def solution(bridge_length, weight, truck_weights):
    queue = deque(truck_weights)
    answer = 0

    ing = deque()
    i = 0
    while queue:
        if ing and i - ing[0][1] >= bridge_length:
            ing.popleft()

        if sum(pair[0] for pair in ing) <= weight - queue[0]:
            ing.append((queue.popleft(), i))
        i += 1
    
    answer = i + bridge_length
    return answer