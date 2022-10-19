#2164

from collections import deque
items = deque(i for i in range(1, int(input())+1))
N = len(items) - 1
for i in range(N):
    items.popleft()
    x = items.popleft()
    items.append(x)

print(items[0])
