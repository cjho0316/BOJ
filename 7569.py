#7569

from collections import deque

T, queue = [], deque()
N, M, H = map(int, input().split())
for _ in range(H):
    K = []
    for i in range(M):
        K.append(list(map(int, input().split())))
    T.append(K)
dx = [1, 0, -1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

for k in range(H):
    for i in range(M):
        for j in range(N):
            if T[k][i][j] == 1:
                queue.append((k, i, j))
                
while queue:
    z, y, x = queue.popleft()
    for s in range(6):
        nx = x + dx[s]
        ny = y + dy[s]
        nz = z + dz[s]
        if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and T[nz][ny][nx] == 0:
            T[nz][ny][nx] = T[z][y][x] + 1
            queue.append((nz, ny, nx))

l = -9999999999
flag = 1
for b in range(H):
    for c in range(M):
        for d in range(N):
            if flag == 1:
                if T[b][c][d] == -1:
                    continue
                elif T[b][c][d] == 0:
                    flag = -1
                    l = 0
                    break
                elif T[b][c][d] > l:
                    l = T[b][c][d]
print(l - 1)
