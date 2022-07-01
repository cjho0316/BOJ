# 1269
import sys

# input_init

N, M = map(int, sys.stdin.readline().rstrip().split())

S = set(map(int, sys.stdin.readline().rstrip().split()))
K = set(map(int, sys.stdin.readline().rstrip().split()))

print(len(S-K) + len(K-S))
