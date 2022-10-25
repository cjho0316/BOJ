#15828
from collections import deque
import sys
M = deque()
N = int(sys.stdin.readline())
x = 0
while True:
    x = int(sys.stdin.readline())
    if x == -1:
        break
    elif x == 0:
        M.popleft()
    elif len(M) == N:
        pass
    elif len(M) < N:
        M.append(x)

if len(M) != 0:
    K = list(M)
    print(*K)
else:
    print('empty')
