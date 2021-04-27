'''
https://programmers.co.kr/learn/courses/30/lessons/42627
heapq
'''

import heapq

def solution(jobs):
    jobs_len = len(jobs)
    jobs.sort(key=lambda x:x[0])
    line = []
    answer = 0
    i = 0

    while jobs or line:
        while jobs:
            item = heapq.heappop(jobs)
            if item[0] <= i:
                heapq.heappush(line, [item[1], item[0]])
            else:
                heapq.heappush(jobs, item)
                break
        
        if line:
            ing = heapq.heappop(line)
            i += ing[0]
            answer += i - ing[1]
        else:
            i += 1
    
    return answer//jobs_len