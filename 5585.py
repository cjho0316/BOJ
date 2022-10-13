#5585

cnt = 0
N = [500, 100, 50, 10, 5, 1]

A = 1000 - int(input())
for i in N:
    if A == 0:
        break
    cnt += A // i
    A %= i
print(cnt)
