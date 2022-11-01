#1966
from collections import deque
N = int(input())

for i in range(N):
    cnt = 0
    x, y = map(int, input().split())
    M = [[i]*2 for i in range(x)]
    S = list(map(int, input().split()))
    for j in range(x):
        M[j][0] = S[j]
    K = deque(M)
    while True:
        rot = 0
        mval = K[0][0]
        molru = K[0][1]
        for i in range(len(K)):
            if mval < K[i][0]:
                mval = K[i][0]
                molru = K[i][1]
                rot = i
            else:
                pass
        K.rotate(-rot)
        t = K.popleft()
        cnt += 1
        if t[1] == y:
            print(cnt)
            break
