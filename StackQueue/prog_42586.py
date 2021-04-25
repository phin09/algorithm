'''
https://programmers.co.kr/learn/courses/30/lessons/42586
queue
'''

from collections import deque

def solution(progresses, speeds):
    answer = []
    queue = deque()
    for i in range(len(speeds)):
        queue.append((progresses[i], speeds[i])) # 작업 진도와 속도를 쌍으로 넣음
    
    day = 0
    num = 0 # 한 번에 배포되는 기능 수
    while len(queue) != 0: # 기능 전부 배포할 때까지 반복
        if queue[0][0] + queue[0][1] * day >= 100: 
            queue.popleft() # deque의 맨 왼쪽 요소의 작업 진도가 100 이상이면 배포
            num = num + 1
        else:
            if num != 0: # 배포할 기능이 있고 그 다음 기능의 작업 진도가 100 미만이면
                answer.append(num) # 하루에 배포한 기능 개수를 answer에 넣음
                num = 0 # 같은 날 배포할 기능이 더이상 없으니 초기화
            day = day + 1
    answer.append(num) # 마지막 배포의 기능 수를 추가 (while 내에서는 배포 직후 빠져 나감)
        
    return answer


# queue를 안 쓴 풀이
# def solution(progresses, speeds):
#     days = []
#     for i in range(len(progresses)):
#         temp = (100 - progresses[i]) // speeds[i]
#         if (100 - progresses[i]) % speeds[i]:
#             d = temp + 1
#         else:
#             d = temp
#         days.append(d)
        
#     answer = []
#     pivot = days[0]
#     cnt = 1
#     for i in range(1, len(days)):
#         if days[i] > pivot:
#             answer.append(cnt)
#             pivot = days[i]
#             cnt = 1
#         else:
#             cnt += 1
    
#     if cnt:
#         answer.append(cnt)
        
#     return answer