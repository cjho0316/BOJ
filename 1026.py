#1026

i = 0
cnt = 0
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
B.reverse()
for i in range(N):
    cnt += A[i] * B[i]
print(cnt)
