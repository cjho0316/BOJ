#11286

import heapq
import sys

input = sys.stdin.readline

N = int(input())
h = []

for i in range(N):
    s = int(input())
    if s == 0 and len(h) == 0:
        print('0')
    elif s == 0:
        print(heapq.heappop(h)[1])
    else:
        heapq.heappush(h, (abs(s), s))
