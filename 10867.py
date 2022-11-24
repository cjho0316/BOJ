#10867

N = int(input())
K = list(set(list(map(int, input().split()))))
K.sort()
print(*K)
