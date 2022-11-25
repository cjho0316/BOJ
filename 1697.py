#1697
from collections import deque

def bfs(a, b):
    sec = 0
    N = [0] * 200001
    queue = deque()
    queue.append([a])
    while queue:
        k = set()
        t = queue.popleft()
        for i in t:
            if b == i:
                return(sec)
            N[i] = 1
            if i-1 >= 0:
                if N[i-1] == 0:
                    k.add(i-1)
                    N[i-1] = 1
            if i+1 <= 100000:
                if N[i+1] == 0:
                    k.add(i+1)
                    N[i+1] = 1
            if i*2 <= 100000:
                if N[i*2] == 0:
                    k.add(i*2)
                    N[i*2] = 1
        if not queue:
            sec += 1
            k = tuple(k)
            queue.append(k)

a, b = map(int, input().split())

print(bfs(a, b))
