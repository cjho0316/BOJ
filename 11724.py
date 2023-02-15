#11724

from collections import deque

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

cnt = 0
N, M = map(int, input().split())
K = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    K[a].append(b)
    K[b].append(a)

for i in range(1, N+1):
    if not visited[i]:
        if not K[i]:
            cnt += 1
            visited[i] = True
        else:
            bfs(K, i, visited)
            cnt += 1

print(cnt)
