#11866

from collections import deque
N, K = map(int, input().split())
S = deque(i for i in range(1, N+1))
M = list()
j = 1
while len(S) > 0:
    if j % K == 0:
        M.append(S.popleft())
    else:
        x = S.popleft()
        S.append(x)
    j += 1

print("<" + ", ".join(list(map(str, M))) + ">")
