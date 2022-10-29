#2346

from collections import deque
N = int(input())
M = [[i]*2 for i in range(1, N+1)]
K = list(map(int, input().split()))
for i in range(N):
    M[i][1] = K[i]
S = deque(M)

j = 1
while len(S) > 0:
    x = S.popleft()
    print(x[0], end=' ')
    if x[1] > 0 and len(S) > 0:
        S.rotate(1-x[1])
    elif x[1] < 0 and len(S) > 0:
        S.rotate(-x[1])
