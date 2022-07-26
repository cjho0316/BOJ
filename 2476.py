#2476
T = int(input())
lmax = -10000
while(T):
    num = 0
    N, M, L = map(int, input().split())
    if N == M == L:
        num += 10000+N*1000
    elif N == M:
        num += 1000+N*100
    elif N == L:
        num += 1000+N*100
    elif M == L:
        num += 1000+M*100
    else:
        num += max(N, M, L)*100
    if lmax < num:
        lmax = num
    T -= 1
print(lmax)
