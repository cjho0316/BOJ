#13458
import math

cnt = 0
N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

for i in A:
    cnt += math.ceil((i - B) / C)

print(cnt + N)
