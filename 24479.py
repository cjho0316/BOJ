#24479
import sys
sys.setrecursionlimit(10**6)

def dfs(graph, visited, v):
    global cnt
    visited[v] = cnt
    graph[v].sort()
    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            dfs(graph, visited, i)

global cnt
cnt = 1
N, M, R = map(int, sys.stdin.readline().split())
visited = [0] * (N+1)
K = [[] for i in range(N+1)]

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    K[x].append(y)
    K[y].append(x)

dfs(K, visited, R)

print(*visited[1:])
