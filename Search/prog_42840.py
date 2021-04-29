'''
https://programmers.co.kr/learn/courses/30/lessons/42840
완전탐색
'''

def solution(answers):
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4 ,5, 5]
    score = [0, 0, 0]
    answer = []
    
    for i in range(len(answers)):
        if answers[i] == student1[i%len(student1)]:
            score[0] += 1
        if answers[i] == student2[i%len(student2)]:
            score[1] += 1
        if answers[i] == student3[i%len(student3)]:
            score[2] += 1
    
    for k in range(len(score)):
        if score[k] == max(score):
            answer.append(k+1)
        
    return answer