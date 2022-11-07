#24444

from collections import deque

def bfs(graph, v, visited):
    cnt = 1
    queue = deque([v])
    visited[v] = cnt
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                cnt += 1
                visited[i] = cnt
                queue.append(i)

N, M, R = map(int, input().split())
K = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
for i in range(M):
    x, y = map(int, input().split())
    K[x].append(y)
    K[y].append(x)

for j in range(N+1):
    K[j].sort()

bfs(K, R, visited)
print(*visited[1:])
