#1931

cnt = 0
start = 0
finish = 0
N = int(input())

M = [[0]*2 for _ in range(N)]
for i in range(N):
    a, b = map(int, input().split())
    M[i][0] = a
    M[i][1] = b

M.sort(key=lambda x: (x[1], x[0]))

for i in range(N):
    if i == 0:
        start = M[0][0]
        finish = M[0][1]
        cnt += 1
    elif finish <= M[i][0]:
        start = M[i][0]
        finish = M[i][1]
        cnt += 1

print(cnt)
