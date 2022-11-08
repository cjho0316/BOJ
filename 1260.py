#1260
from collections import deque


def dfs(graph1, v, visited1):
    global cnt
    graph1[v].sort()
    visited1[v] = cnt
    for i in graph1[v]:
        if not visited1[i]:
            cnt += 1
            dfs(graph1, i, visited1)


def bfs(graph2, v, visited2):
    cnt1 = 1
    visited2[v] = cnt1
    queue = deque([v])
    while queue:
        v = queue.popleft()
        for i in graph2[v]:
            if not visited2[i]:
                queue.append(i)
                cnt1 += 1
                visited2[i] = cnt1


global cnt
cnt = 1
N, M, V = map(int, input().split())
K = [[] for _ in range(N+1)]
visited1 = [0 for _ in range(N+1)]
visited2 = [0 for _ in range(N+1)]

for i in range(M):
    x, y = map(int, input().split())
    K[x].append(y)
    K[y].append(x)

dfs(K, V, visited1)
bfs(K, V, visited2)
S1, T1 = list(), list()

S = [[0]*2 for _ in range(N+1)]
for i in range(N+1):
    S[i][0] = i
    S[i][1] = visited1[i]
S.sort(key=lambda x: (x[1], x[0]))

T = [[0]*2 for _ in range(N+1)]
for j in range(N+1):
    T[j][0] = j
    T[j][1] = visited2[j]
T.sort(key=lambda x: (x[1], x[0]))

for i in range(1, len(S)):
    if S[i][1] != 0:
        S1.append(S[i][0])
    if T[i][1] != 0:
        T1.append(T[i][0])

print(*S1[-M-1:])
print(*T1[-M-1:])
