#5014
from collections import deque

def bfs(F, K, S, G, cnt):
    queue = deque()
    queue1 = deque()
    queue.append(S)
    while queue:
        v = queue.popleft()
        K[v] = 1
        if G == v:
            return(cnt)
        if cnt == 0:
            cnt += 1

        nu = v+U
        nd = v-D
        if nu > F and nd < 1 :
            return

        if nu <= 1000000 and K[nu] == 0:
            K[nu] = 1
            queue1.append(nu)

        if nd >=1 and K[nd] == 0:
            K[nd] = 1
            queue1.append(nd)
        
        if G == nu or G == nd:
            return(cnt)
            
        if not queue:
            queue = queue1
            queue1 = deque()
            cnt += 1

cnt = 0
F,S,G,U,D = map(int, input().split())
K = [0] * 1000001
t = bfs(F, K, S, G, cnt)
if K[G] != 1:
    print('use the stairs')
else:
    print(t)
