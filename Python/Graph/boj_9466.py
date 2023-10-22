# https://www.acmicpc.net/problem/9466

# https://claude-u.tistory.com/435
# 이거랑 비교해가며 시간초과의 원인을 찾기
# -> 지금 상태론 일부 닫힌사이클을 미리 발견해도 걍 무시하고 무조건 모든 원소를 시작으로 도는 걸 다 해보네...


# 시간 초과
# import sys
#
#
# def dfs(node, __graph):
#     __visited = []
#     stack = [node]
#     while stack:
#         curr = stack.pop()
#         __visited.append(curr)
#         next = __graph[curr]
#         if node == next:
#             return __visited
#         elif next in __visited or done[next] == 1:
#             return []
#         else:
#             stack.append(next)
#
#
# t = int(sys.stdin.readline())   # 테스트 케이스 개수
#
# for _ in range(t):
#     n = int(sys.stdin.readline())   # 학생의 수
#     inputArr = list(map(int, sys.stdin.readline().split(' ')))
#     graph = [0] * (n+1)
#     for i in range(1, n+1):
#         graph[i] = inputArr[i-1]
#
#     done = [0] * (n+1)
#     for i in range(1, n+1):
#         if done[i] == 0:
#             for j in dfs(i, graph):
#                 done[j] = 1
#
#     print(n - sum(done))



# 더 심하게 시간 초과
# import sys
#
#
# def dfs(node):
#     visited = []
#     stack = [node]
#     while stack:
#         curr = stack.pop()
#         visited.append(curr)
#         next = graph[curr]
#         if node == next:
#             return visited
#         elif next in visited:
#             return []
#         else:
#             stack.append(next)
#
#
# t = int(sys.stdin.readline())   # 테스트 케이스 개수
#
# for _ in range(t):
#     n = int(sys.stdin.readline())   # 학생의 수
#     inputArr = list(map(int, sys.stdin.readline().split(' ')))
#     graph = [0] + inputArr
#
#     done = []
#     for i in range(1, n+1):
#         if i not in done:
#             done += dfs(i)
#
#     print(n - len(done))