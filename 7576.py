# 7576
from collections import deque

K, queue = [], deque()
N, M = map(int, input().split())
for i in range(M):
    K.append(list(map(int, input().split())))
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for i in range(M):
    for j in range(N):
        if K[i][j] == 1:
            queue.append((i, j))
            
while queue:
    y, x = queue.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and K[ny][nx] == 0:
            K[ny][nx] = K[y][x] + 1
            queue.append((ny, nx))

l = -9999999999
flag = 1
for c in range(M):
    for d in range(N):
        if flag == 1:
            if K[c][d] == -1:
                continue
            elif K[c][d] == 0:
                flag = -1
                l = 0
                break
            elif K[c][d] > l:
                l = K[c][d]
print(l - 1)
