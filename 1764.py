# 1764
import sys

# input_init
S, K = set(), set()
N, M = map(int, sys.stdin.readline().rstrip().split())

for i in range(N):
    S.add(sys.stdin.readline().rstrip())
for j in range(M):
    K.add(sys.stdin.readline().rstrip())

T = list(S & K)
T.sort()

print(len(T))
for i in T: print(i)
