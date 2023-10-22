'''
https://programmers.co.kr/learn/courses/30/lessons/42579

nested list 안에서 첫번째 값 합하기
https://www.python2.net/questions-39770.htm
sum(zip(*l)[0]) 썼다가 아래 에러가 남.
TypeError: 'zip' object is not subscriptable
이 에러가 나기 전후에 dict.items()에서 items()를 빼먹은 걸 깨닫고 넣었었는데, 위 에러의 원인이 이거였는지 확인해보기.

lambda 공부하기.
'''

def solution(genres, plays):
    genre_song = {}
    for i in range(len(genres)):
        if genres[i] in genre_song:
            genre_song[genres[i]].append([i, plays[i]])
        else:
            genre_song[genres[i]] = [[i, plays[i]]]
        
    genre_cnt = []
    for key, value in genre_song.items():
        genre_cnt.append([key, sum(i[1] for i in value)])
        
    genre_cnt.sort(key=lambda x:x[1], reverse=True)
    answer = []
    for genre in genre_cnt:
        temp = sorted(genre_song[genre[0]], key=lambda x:x[1], reverse=True)
        answer.append(temp[0][0])
        if len(temp) > 1:
            answer.append(temp[1][0])
        
    return answer