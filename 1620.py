#1620
import sys
#input_init
N, M = map(int, sys.stdin.readline().rstrip().split())
S = dict()
for _ in range(N):
    key = _
    val = sys.stdin.readline().rstrip()
    S[key] = val
    
rev_S = dict((value, key) for (key, value) in S.items())

for i in range(M):
    K = sys.stdin.readline().rstrip()
    if K.isdigit():
        K = int(K)
        print(S[K-1])
    else:    
        print(rev_S[K]+1)
