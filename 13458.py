#13458
import math

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = 0
for a in A:
    if a > B:
        cnt += math.ceil((a - B) / C)
        
print(cnt + N)
