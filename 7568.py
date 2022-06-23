#7568
import sys
#init
N = int(sys.stdin.readline().rstrip())
S = [[0] * 2 for _ in range(N)]
for i in range(len(S)):
    S[i][0], S[i][1] = map(int, sys.stdin.readline().rstrip().split())

#compare
K = [0]*N
for j in range(len(S)):
    for i in range(0, len(S)):
        if S[j][0] < S[i][0] and S[j][1] < S[i][1]:
            K[j] += 1
        else:
            pass
for i in range(len(K)):
    K[i] += 1

#print
print(*K, end=' ')
