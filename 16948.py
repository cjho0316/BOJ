#16948

from collections import deque

def bfs(N, a, b, x, y):
    cnt = 0
    K = [[0]*N for _ in range(N)]
    K[a][b] = 1
    queue = deque()
    queue1 = deque()
    queue.append((a, b))
    while queue:
        a, b = queue.popleft()
        if a == x and b == y:
            return (cnt)
        for j in range(6):
            na = a + dx[j]
            nb = b + dy[j]
            if na > N-1 or na < 0 or nb > N-1 or nb < 0:
                continue
            if K[na][nb] == 1:
                continue
            else:
                K[na][nb] = 1
                queue1.append((na, nb))
        if not queue:
            queue = queue1
            queue1 = deque()
            cnt += 1

N = int(input())
a, b, x, y = map(int, input().split())
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]
k = bfs(N, a, b, x, y)
if k:
    print(k)
else:
    print(-1)
