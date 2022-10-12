#1541
import sys
flag = 0
N = int(sys.stdin.readline())

for i in range(N):
    cnt = 0
    A = int(sys.stdin.readline())
    M = [[0]*2 for _ in range(A)]
    for j in range(A):
        x, y = map(int, sys.stdin.readline().split())
        M[j][0] = x
        M[j][1] = y
    M.sort(key=lambda x: (x[1], x[0]))
    for k in range(A):
        if k == 0:
            flag = M[k][0]
            cnt += 1
        elif flag > M[k][0]:
            cnt += 1
            flag = M[k][0]
    print(cnt)
