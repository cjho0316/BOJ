# 18870

# input_init
N = int(input())
S, T = list(map(int, input().split())), list()
P = dict()
T = S.copy()
T.sort()
cnt = 0


for i in range(len(T)):
    if i == 0:
        P[T[i]] = 0
    if T[i] == T[i-1]:
        continue
    else:
        key = T[i]
        val = cnt
        P[key] = val
        cnt += 1

K = list()

for j in S:
    K.append(P.get(j))

print(*K)
