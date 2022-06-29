# 10989
import sys
# input_init
N = int(sys.stdin.readline().rstrip())
S = [0]*10001

for _ in range(N):
    idx = int(sys.stdin.readline().rstrip())
    S[idx] += 1

#print
for j in range(10001):
    if S[j] > 0:
        for _ in range(S[j]):
            sys.stdout.write(str(j) + '\n')
