#13305

cnt, k, a = 0, 0, 1000000000
N = int(input())
length = list(map(int, input().split()))
station = list(map(int, input().split()))

for i in range(N-1):
    if i == 0:
        a = station[i]
        cnt += a * length[i]
    elif a * length[i] <= station[i] * length[i]:
        cnt += a * length[i]
    elif a * length[i] > station[i] * length[i]:
        a = station[i]
        cnt += a * length[i]

print(cnt)
