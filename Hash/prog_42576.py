'''
https://programmers.co.kr/learn/courses/30/lessons/42576

정렬 후 비교로도 풀어보면 좋을듯.
'''

def solution(participant, completion):
    hashed_completion = {}
    for name in completion:
        if name not in hashed_completion:
            hashed_completion[name] = 1
        else:
            hashed_completion[name] += 1
    
    for name in participant:
        if name in hashed_completion:
            hashed_completion[name] -= 1
            if hashed_completion[name] < 0:
                answer = name
        else:
            answer = name
            
    return answer