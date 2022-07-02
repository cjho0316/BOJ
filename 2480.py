#2480
N, M, L = map(int, input().split())

if N == M == L:
    print(10000 + N*1000)
elif N == M:
    print(1000 + N*100)
elif N == L:
    print(1000 + N*100)
elif M == L:
    print(1000 + M*100)
else:
    print(max(N, M, L)*100)
