'''
https://programmers.co.kr/learn/courses/30/lessons/43162
DFS

문제를 읽고 그래프가 사선을 기준으로 당연히 대칭이 될 거라 생각했는데 아니었다.

union-find로도 풀 수 있다 함.
'''

def solution(n, computers):
    visited = [0 for _ in range(n)]
    answer = 0
    
    def dfs(node):
        visited[node] = 1
        for j in range(n):
            if visited[j] == 0 and computers[node][j] == 1:
                dfs(j)
    
    for i in range(n):
        if visited[i] == 0:
            dfs(i)
            answer += 1
    
    return answer