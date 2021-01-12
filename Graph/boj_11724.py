# https://www.acmicpc.net/problem/11724

# 방법 1 - DFS
# 런타임에러
# import sys
#
# n, m = map(int, sys.stdin.readline().split(' '))
# visited = [0] * (n+1)
# graph = [[0]*(n+1) for _ in range(n+1)]
#
# for _ in range(m):
#     a, b = map(int, sys.stdin.readline().split(' '))
#     graph[a][b] = 1
#     graph[b][a] = 1
# cnt = 0
#
# def dfs(node):
#     visited[node] = 1
#     for i in range(1, n+1):
#         if visited[i] == 0 and graph[node][i] == 1:
#             dfs(i)
#
# for i in range(1, n+1):
#     if visited[i] == 1:
#         continue
#     else:
#         dfs(i)
#         cnt += 1
#
# print(cnt)

# 방법 2 - BFS. 속도 엄청 느림
import sys

n, m = map(int, sys.stdin.readline().split(' '))
visited = []
graph = {}
for i in range(1, n+1):
    graph[i] = []

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split(' '))
    graph[a].append(b)
    graph[b].append(a)

cnt = 0

def bfs(node):
    queue = [node]
    while queue:
        v = queue.pop(0)
        for item in graph[v]:
            if item not in visited:
                visited.append(item)
                queue.append(item)

for i in range(1, n+1):
    if i in visited:
        continue
    else:
        bfs(i)
        cnt += 1

print(cnt)