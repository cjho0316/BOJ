#10866
import sys
from collections import deque
items = deque()

def push_front(x):
    items.append(x)

def push_back(x):
    items.appendleft(x)

def pop_front():
    if empty(): return -1
    else: return items.pop()

def pop_back():
    if empty(): return -1
    else: return items.popleft()

def size():
    return len(items)

def empty():
    if not items : return 1
    else : return 0

def front():
    if empty(): return -1
    else: return items[len(items) - 1]

def back():
    if empty(): return -1
    else: return items[0]

for i in range(int(input())):
    S = sys.stdin.readline().rstrip().split()
    if S[0] == 'push_front': push_front(S[1])
    elif S[0] == 'push_back': push_back(S[1])
    elif S[0] == 'pop_front': print(pop_front())
    elif S[0] == 'pop_back': print(pop_back())
    elif S[0] == 'size': print(size())
    elif S[0] == 'empty': print(empty())
    elif S[0] == 'front': print(front())
    elif S[0] == 'back': print(back())
