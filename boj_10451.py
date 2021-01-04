# https://www.acmicpc.net/problem/10451

# https://claude-u.tistory.com/434
import sys
sys.setrecursionlimit(2000)

def dfs(node, __visited, graph):
    __visited[node] = 1
    curr = graph[node]
    if __visited[curr] == 0:    # 순열은 한개당 하나씩 이어져 있으니 for문 필요 없음.
        dfs(curr, __visited, graph)

t = int(sys.stdin.readline())   # 테스트 케이스 개수
for _ in range(t):
    n = int(sys.stdin.readline())   # 수열의 길이
    inputArr = [0] + list(map(int, sys.stdin.readline().split(' ')))
    visited = [0] * (n+1)
    cnt = 0

    for i in range(1, n+1):
        if visited[i] == 0:
            dfs(i, visited, inputArr)
            cnt += 1

    print(cnt)

# 시간 초과
# import sys
#
# def checkDFS(node, visited):
#     global cnt
#     stack = [node]
#     while stack:
#         curr = stack.pop()
#         if curr not in visited:
#             visited.append(curr)
#             stack.extend(list(set(graph[curr]) - set(visited)))
#     cnt += 1
#     return visited
#
# t = int(sys.stdin.readline())   # 테스트 케이스 개수
#
# for i in range(t):
#     n = int(sys.stdin.readline())   # 순열의 크기
#     inputArr = list(map(int, sys.stdin.readline().split(' ')))
#     graph = {}
#     for j in range(n):
#         if (j+1) in graph:
#             graph[j+1] += [inputArr[j]]
#         else:
#             graph[j+1] = [inputArr[j]]
#
#     cnt = 0
#     visited = []
#     for k in range(1, n+1):
#         if k not in visited:
#             visited = checkDFS(k, visited)
#
#     print(cnt)