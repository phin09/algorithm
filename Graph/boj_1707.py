# https://www.acmicpc.net/problem/1707

# https://www.acmicpc.net/source/24838452
# 성준님 풀이 참고해서 다시 풀기


# 시간 초과
# import sys
# from collections import deque
#
#
# def checkB(_v, _graph, _color):
#     for node in range(1, _v+1):
#         for target in _graph[node]:
#             if _color[node] == _color[target]:
#                 return 0    # 이분 그래프 아님
#     return 1    # 이분그래프
#
#
# def bfs(start, __v, __graph, __color, __visited):
#     __visited[start] = 1
#     __color[start] = 1
#     queue = deque([start])
#     while queue:
#         node = queue.popleft()
#         for i in range(1, v+1):
#             if __visited[i] == 0 and i in __graph[node]:
#                 __visited[i] = 1
#                 if __color[node] == 1:
#                     __color[i] = 2
#                 else:
#                     __color[i] = 1
#                 queue.extendleft(__graph[i])
#
#     if checkB(__v, __graph, __color) == 1:
#         return 1
#     else:
#         return 0
#
#
# k = int(sys.stdin.readline())   # 테스트 케이스 개수
#
# for i in range(k):
#     v, e = map(int, sys.stdin.readline().split(' '))  # node 수, 간선 수
#     graph = {}
#     for i in range(1, v+1):
#         graph[i] = []
#     for _ in range(e):
#         a, b = map(int, sys.stdin.readline().split(' '))
#         graph[a].append(b)
#         graph[b].append(a)
#
#     visited = [0] * (v+1)
#     color = [0] * (v+1)
#
#     if bfs(1, v, graph, color, visited) == 1:
#         print('YES')
#     else:
#         print('NO')