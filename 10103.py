#10103

N = int(input())
X, Y = 100, 100
for i in range(N):
    a, b = map(int, input().split())
    if a == b:
        continue
    elif a > b:
        Y -= a
    elif a < b:
        X -= b
print(X)
print(Y)
