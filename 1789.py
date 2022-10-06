#1789

cnt = 0
N = int(input())

if N == 1:
    cnt += 1

for i in range(1, N):
    if N >= i:
        N -= i
    else:
        break
    cnt += 1
print(cnt)
