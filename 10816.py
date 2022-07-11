# 10816

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
        P[T[i]] += 1
    else:
        key = T[i]
        val = 1
        P[key] = val

K = list()

M = int(input())
K, Q = list(map(int, input().split())), list()

for j in K:
    a = P.get(j)
    if a == None:
        a = 0
    Q.append(a)

print(*Q)
