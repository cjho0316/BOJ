#18258
import sys
from collections import deque
items = deque()


def push(a):
    items.append(a)


def pop():
    if empty():
        return -1
    else:
        return items.popleft()


def size():
    return len(items)


def empty():
    if not items:
        return 1
    else:
        return 0


def front():
    if empty():
        return -1
    else:
        return items[0]


def back():
    if empty():
        return -1
    else:
        return items[len(items)-1]


for i in range(int(sys.stdin.readline())):
    S = sys.stdin.readline().rstrip().split()
    if S[0] == 'push':
        push(S[1])
    elif S[0] == 'pop':
        print(pop())
    elif S[0] == 'size':
        print(size())
    elif S[0] == 'empty':
        print(empty())
    elif S[0] == 'front':
        print(front())
    elif S[0] == 'back':
        print(back())
