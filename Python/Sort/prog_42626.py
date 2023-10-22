'''
https://programmers.co.kr/learn/courses/30/lessons/42626
heapq 모듈 사용

맨 처음으로 heappop할 때 힙정렬을 하지 않고 바로 맨 앞 값을 뽑아준다.
대상 리스트가 힙정렬이 되지 않은 상태면 틀린다.
heapq.heapify 사용.

PriorityQueue로 풀면 시간 초과.
'''

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
        
    while True:
        min = heapq.heappop(scoville)
        if min < K:
            if scoville:
                heapq.heappush(scoville, min + 2*heapq.heappop(scoville))
                answer += 1
            else:
                return -1
        else:
            break
    
    return answer