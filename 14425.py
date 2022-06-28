#14425
#input_init
N, M = map(int, input().split())
S = set(input() for _ in range(N))
K = list(input() for _ in range(M))
cnt = 0

#search
for i in K:
    if i in S:
        cnt += 1

#print
print(cnt)
