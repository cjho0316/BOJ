#5063
N = int(input())

for i in range(N):
    A, B, C = map(int, input().split())
    if A > B-C:
        print("do not advertise")
    elif A == B-C:
        print("does not matter")
    else:
        print("advertise")
