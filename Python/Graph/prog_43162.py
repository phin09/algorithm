'''
https://programmers.co.kr/learn/courses/30/lessons/43162
DFS

문제를 읽고 그래프가 사선을 기준으로 당연히 대칭이 될 거라 생각했는데 아니었다.

union-find로도 풀 수 있다 함.
'''

# DFS

# def solution(n, computers):
#     visited = [0 for _ in range(n)]
#     answer = 0
    
#     def dfs(node):
#         visited[node] = 1
#         for j in range(n):
#             if visited[j] == 0 and computers[node][j] == 1:
#                 dfs(j)
    
#     for i in range(n):
#         if visited[i] == 0:
#             dfs(i)
#             answer += 1
    
#     return answer


# union-find

def get_parent(lst, a):
    if lst[a] == a:
        return a
    lst[a] = get_parent(lst, lst[a])
    return lst[a]
    
    
def union_parent(lst, a, b):
    x = get_parent(lst, a)
    y = get_parent(lst, b)
    if x < y:
        lst[y] = x
    else:
        lst[x] = y
    

def solution(n, computers):
    parents = [k for k in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                union_parent(parents, i, j)
    
    answer = []
    for k in parents:
        answer.append(get_parent(parents, k))
        
    return len(set(answer))