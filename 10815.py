#10815
#init
N = int(input())
S = set(map(int, input().split()))
M = int(input())
K = list(map(int, input().split()))

#find
for i in range(len(K)):
    if K[i] in S:
        K[i] = 1
    else:
        K[i] = 0   

#print
print(*K)
