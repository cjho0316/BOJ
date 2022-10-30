#2238

M, N = map(int, input().split())

A = [[0]*N for _ in range(M)]
for i in range(M):
    A[i] = list(map(int, input().split()))
B = [[0]*N for _ in range(M)]
for j in range(M):
    B[j] = list(map(int, input().split()))

for x in range(M):
    for y in range(N):
        print(A[x][y]+B[x][y], end = ' ')
