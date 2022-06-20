import math
N, K = map(int, input().split())
n = 1
for i in range(K):
    n *= N-i
k = math.factorial(K)
print(int(n // k) % 10007)
