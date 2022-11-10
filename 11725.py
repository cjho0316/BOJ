#11725
import sys
sys.setrecursionlimit(10**6)
def dfs(graph, v, vistied):
    for i in graph[v]:
        if not visited[i]:
            visited[i] = v
            dfs(graph, i, visited)

N = int(input())
K = [[] for i in range(N+1)]
visited = [False] * (N+1)
for i in range(N-1):
    a, b = map(int, input().split())
    K[a].append(b)
    K[b].append(a)

dfs(K, 1, visited)
print(*visited[2:])
