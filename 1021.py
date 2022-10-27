#1021
from collections import deque
N, M = map(int, input().split())
K = deque(i for i in range(1, N+1))
T = list(map(int, input().split()))
cnt = 0

for i in T:
    idx = K.index(i)
    left, right = 0, 0
    if idx > len(K) - idx:
        K.rotate((len(K)-idx))
        right = len(K)-idx
    else:
        K.rotate(-idx)
        left = idx
    K.popleft()
    cnt += (left + right)

print(cnt)
