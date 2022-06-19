#2108
from collections import Counter
import sys
#init
N = int(sys.stdin.readline().rstrip())
S = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
S.sort()
#mean
print(int(round(sum(S)/N, 0)))
#median
print(S[int(len(S)/2)])
#mode
k = Counter(S).most_common()
if N > 1:
    if k[0][1] == k[1][1]:
        print(k[1][0])
    else:
        print(k[0][0])
else:
    print(k[0][0])
#range
print(S[len(S) - 1] - S[0])
