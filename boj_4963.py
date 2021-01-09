# https://www.acmicpc.net/problem/4963

# boj 2667 푼 방법. 가로 세로 range를 어떻게 돌리는지 주의해야 됨.
import sys
sys.setrecursionlimit(2000)


def dfs(x, y):
    visited[x][y] = True

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w:
            if graph[nx][ny] == 1 and visited[nx][ny] is False:
                    dfs(nx, ny)


while True:
    w, h = map(int, sys.stdin.readline().split(' '))
    if w == 0 and h == 0:
        break

    graph = [0 for _ in range(h)]
    for i in range(h):
        graph[i] = list(map(int, sys.stdin.readline().split(' ')))

    visited = [[False for _ in range(w)] for _ in range(h)]

    # 8방향
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

    cnt = 0
    for a in range(h):
        for b in range(w):
            if graph[a][b] == 1 and visited[a][b] is False:
                dfs(a, b)
                cnt += 1

    print(cnt)



# 틀리고 index 에러도 남
# import sys
#
#
# def DFS(i, j):
#     def rDFS(i, j):
#         if graph[i][j] == 1 and visited[i][j] is False:
#             visited[i][j] = True
#
#             if i < w-1 and graph[i+1][j] == 1 : rDFS(i+1, j)  # 아래
#             if i > 0 and graph[i-1][j] == 1: rDFS(i-1, j) # 위
#             if j < h-1 and graph[i][j+1] == 1: rDFS(i, j+1)   # 오른쪽
#             if j > 0 and graph[i][j-1] == 1: rDFS(i, j-1) # 왼쪽
#             if i < j-1 and j > 0 and graph[i+1][j-1] == 1: rDFS(i+1, j-1)   # 왼쪽 아래 대각선
#             if i > 0 and j > 0 and graph[i-1][j-1] == 1: rDFS(i-1, j-1)  # 왼쪽 위 대각선
#             if i > 0 and j < h-1 and graph[i-1][j+1] == 1: rDFS(i-1, j+1)   # 오른쪽 위 대각선
#             if i < j-1 and j < h-1 and graph[i+1][j+1] == 1: rDFS(i+1, j+1) # 오른쪽 아래 대각선
#
#     rDFS(i, j)
#
#
# while True:
#     w, h = map(int, sys.stdin.readline().split(' '))
#     if w == 0 and h == 0:
#         break
#     graph = [0] * h
#     for i in range(h):
#         graph[i] = list(map(int, sys.stdin.readline().split(' ')))
#
#     visited = [[False for _ in range(w)] for _ in range(h)]
#     cnt = 0
#     for i in range(w):
#         for j in range(h):
#             if graph[i][j] == 1 and visited[i][j] is False:
#                 cnt += 1
#
#     print(cnt)