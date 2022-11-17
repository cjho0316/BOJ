#17219
N, M = map(int, input().split())
A = dict()
for i in range(N):
    i, v = tuple(input().split())
    A[i] = v
    
for _ in range(M):
    B = str(input())
    print(A[B])
