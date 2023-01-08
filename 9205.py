#9205
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        v1, v2 = queue.popleft()
        if abs(v1-c) + abs(v2-d) <= 1000:
            print('happy')
            return
        for i in range(N):
            if not visited[i]:
                nv1, nv2 = graph[i]
                if abs(nv1-v1) + abs(nv2-v2) <= 1000:
                    visited[i] = 1
                    queue.append((nv1, nv2))
    print('sad')
    return

T = int(input())

for i in range(T):
    N = int(input())
    a, b = map(int, input().split())
    graph = []
    for j in range(N):
        x, y = map(int, input().split())
        graph.append((x, y))
    c, d = map(int, input().split())
    visited = [0] * (N+1)
    bfs(a, b)
        
