# # https://www.acmicpc.net/problem/1260
# # global 선언 없이도 함수에서 쓸 수 있는 변수들 있음. 일단 그냥 쓰긴 했는데 이걸 그대로 놔둬도 되는 건지?
#
# # 방법 1
# # https://pilyeooong.tistory.com/196
# import sys
#
# n, m, v = map(int, sys.stdin.readline().split(' '))
# graph = [[0] * (n+1) for _ in range(n+1)]
# visited = [0] * (n+1)
#
# for _ in range(m):
#     a, b = map(int, sys.stdin.readline().split(' '))
#     graph[a][b] = 1
#     graph[b][a] = 1
#
# def dfs(node):
#     visited[node] = 1   # 방문한 node를 1로 표시
#     print(node, end=' ')
#     for i in range(1, n+1):
#         if visited[i] == 0 and graph[node][i] == 1:
#             dfs(i)
#
# def bfs(node):
#     visited[node] = 0   # dfs를 거치며 전부 1로 되어있는 상태라 이젠 방문한 node를 0으로 표시
#     queue = [node]
#     while queue:
#         v = queue.pop(0)
#         print(v, end=' ')
#         for i in range(1, n+1):
#             if visited[i] and graph[v][i]:
#                 visited[i] = 0
#                 queue.append(i)
#
# dfs(v)
# print() # \n
# bfs(v)
#
# # 방법 2 - collections.deque
# import sys
# from collections import deque
#
# n, m, v = map(int, sys.stdin.readline().split(' '))
# graph = [[0] * (n+1) for _ in range(n+1)]
# visited = [0] * (n+1)
#
# for _ in range(m):
#     a, b = map(int, sys.stdin.readline().split(' '))
#     graph[a][b] = 1
#     graph[b][a] = 1
#
# def dfs(node):
#     visited[node] = 1   # 방문한 node를 1로 표시
#     print(node, end=' ')
#     for i in range(1, n+1):
#         if visited[i] == 0 and graph[node][i] == 1:
#             dfs(i)
#
# def bfs(node):
#     visited[node] = 0   # dfs를 거치며 전부 1로 되어있는 상태라 이젠 방문한 node를 0으로 표시
#     queue = deque([node])
#     while queue:
#         v = queue.popleft()
#         print(v, end=' ')
#         for i in range(1, n+1):
#             if visited[i] and graph[v][i]:
#                 visited[i] = 0
#                 queue.append(i)
#
# dfs(v)
# print() # \n
# bfs(v)
#
# # 방법 3 - collections.deque
# # https://juhee-maeng.tistory.com/28
# # graph를 간선을 정리한 dict형태로 만들어서 deque 운용이 더 효율적이게 한 방법
#
# import sys
# from collections import deque
#
# n, m, v = map(int, sys.stdin.readline().split(' ')) # node 개수, 간선 개수, start node
# graph = {}
# for _ in range(m):
#     a, b = map(int, sys.stdin.readline().split(' '))
#     if a in graph:
#         graph[a].append(b)
#     else:
#         graph[a] = [b]
#     # graph[a] += [b] # if문 없이 이거만 있어도 되는지 테스트해보고 싶은 부분 => 안 됨
#
# visited = []
# stack = deque([v])
# while stack:
#     node = stack.popleft()  # 지금 방문하는 곳 pop
#     if node not in visited:
#         visited.append(node)
#         stack.extend(graph[node])   # 연결된 node들을 stack에 추가
#
# print(visited)


# 추가
# stack에 중복 node가 여러번 들어가는데 set으로 쓰면 안 되나? => set을 바로 stack으로 쓰는 건 위험함
# https://dojang.io/mod/forum/discuss.php?d=797
# set에서 pop하면 임의의 원소를 삭제, 반환한다.
import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split(' '))
graph = {}
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split(' '))
    if a in graph:
        graph[a].append(b)
    else:
        graph[a] = [b]

    if b in graph:
        graph[a].append(b)
    else:
        graph[b] = [a]

# dfs
visited = []
stack = [v]
while stack:
    node = stack.pop(0)
    if node not in visited:
        visited.append(node)
        stack.extend(graph[node])

print(' '.join(list(map(str, visited))))

# bfs
visited = []
queue = deque([v])
while queue:
    node = queue.popleft()
    if node not in visited:
        visited.append(node)
        queue.extend(graph[node])
        queue = deque(set(queue))    # 중복제거 효과만 취할 수 있는지.. 기존 순서는 유지되어야. => 되는듯?

# result = ''.join(visited)   # expected str instance, int found. 문자 배열에서만 가능한 방법.
result = list(map(str, visited))
print(' '.join(result))

# # 방법 4 - 어떻게 이렇게 속도가 빠르지?
# # https://www.acmicpc.net/source/24810503