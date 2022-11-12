#2178
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x1, y1 = queue.popleft()
        for i in range(4):
            nx = x1 + dx[i]
            ny = y1 + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if K[nx][ny] == 0:
                continue
            if K[nx][ny] == 1:
                K[nx][ny] = K[x1][y1] + 1
                queue.append((nx, ny))
    return (K[N-1][M-1])

N, M = map(int, input().split())
K = []
for i in range(N):
    K.append(list(map(int, input())))

cnt = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))
