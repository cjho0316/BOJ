#5430
from collections import deque
import sys
N = int(sys.stdin.readline().rstrip())
for i in range(N):
    S = list(str(sys.stdin.readline().rstrip()))
    flag = 0
    cnt = 0
    M = int(sys.stdin.readline().rstrip())
    W = str(sys.stdin.readline().rstrip())
    p = deque(list(W[1:-1].split(',')))
    for j in range(len(S)):
        if S[j] == 'R':
            cnt += 1
        elif S[j] == 'D':
            if len(p) == 0 or M == 0:
                flag = 1
                break
            elif cnt % 2 == 1:
                p.pop()
            else:
                p.popleft()
    if cnt % 2 == 1:
        p.reverse()

    if flag == 1:
        print('error')
    elif flag == 0:
        print("[" + ",".join(map(str, p)) + "]")
