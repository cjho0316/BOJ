#16928
from collections import deque

def bfs(K, dx, i):
    cnt = 1
    queue = deque()
    queue1 = deque()
    queue.append(i)
    while queue:
        v = queue.popleft()
        for i in range(6):
            nx = v + dx[i]
            if nx == 100:
                print(cnt)
                quit()
            elif K[nx] != -1 and K[nx] != 0:
                queue1.append(K[nx])
            elif K[nx] == -1:
                K[nx] = 0
                queue1.append(nx)
        if not queue:
            queue = queue1
            queue1 = deque()
            cnt += 1
        

K = [-1] * 101

N, M = map(int, input().split())

for i in range(N):
    x, y = map(int, input().split())
    K[x] = y
for j in range(M):
    u, v = map(int, input().split())
    K[u] = v
    
dx = [1,2,3,4,5,6]
bfs(K, dx, 1)
