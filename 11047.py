#11047

i = 0
cnt = 0
N, M = map(int, input().split())

K = []
for i in range(N):
    K.append(int(input()))
K.reverse()
for coin in K:
    cnt += M // coin
    M %= coin
print(cnt)
