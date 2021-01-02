# https://www.acmicpc.net/problem/1260
# global 선언 없이도 함수에서 쓸 수 있는 변수들 있음. 일단 그냥 쓰긴 했는데 이걸 그대로 놔둬도 되는 건지?

# 방법 1
# https://pilyeooong.tistory.com/196
import sys

n, m, v = map(int, sys.stdin.readline().split(' '))
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split(' '))
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(node):
    visited[node] = 1   # 방문한 node를 1로 표시
    print(node, end=' ')
    for i in range(1, n+1):
        if visited[i] == 0 and graph[node][i] == 1:
            dfs(i)

def bfs(node):
    visited[node] = 0   # dfs를 거치며 전부 1로 되어있는 상태라 이젠 방문한 node를 0으로 표시
    queue = [node]
    while queue:
        v = queue.pop(0)
        print(v, end=' ')
        for i in range(1, n+1):
            if visited[i] and graph[v][i]:
                visited[i] = 0
                queue.append(i)

dfs(v)
print() # \n
bfs(v)

# 방법 2 - collections.deque
import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split(' '))
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split(' '))
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(node):
    visited[node] = 1   # 방문한 node를 1로 표시
    print(node, end=' ')
    for i in range(1, n+1):
        if visited[i] == 0 and graph[node][i] == 1:
            dfs(i)

def bfs(node):
    visited[node] = 0   # dfs를 거치며 전부 1로 되어있는 상태라 이젠 방문한 node를 0으로 표시
    queue = deque([node])
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if visited[i] and graph[v][i]:
                visited[i] = 0
                queue.append(i)

dfs(v)
print() # \n
bfs(v)

# 방법 3 - collections.deque
# https://juhee-maeng.tistory.com/28
# graph를 간선을 정리한 dict형태로 만들어서 deque 운용이 더 효율적이게 한 방법

# 방법 4 - 어떻게 이렇게 속도가 빠르지?
# https://www.acmicpc.net/source/24810503