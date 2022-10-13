#2217
import sys
xmost = 0
cnt = 0
N = int(sys.stdin.readline())
A = list()
for i in (range(N)):
    A.append(int(sys.stdin.readline()))
A.sort(reverse=True)

B = list()
for i in range(len(A)):
    cnt += 1
    B.append(A[i])
    if xmost < B[i] * cnt:
        xmost = B[i] * cnt
print(xmost)
