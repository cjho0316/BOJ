#1012
import sys
sys.setrecursionlimit(10**6)
def dfs(K, x, y):
    if x<=-1 or x>=M or y<=-1 or y>=N:
        return False
    if K[x][y] == 1:
        K[x][y] = 0
        dfs(K, x-1, y)
        dfs(K, x, y-1)
        dfs(K, x+1, y)
        dfs(K, x, y+1)
        return True
    return False

T = int(input())
for _ in range(T):
    M, N, R = map(int, input().split())
    K = [[0]*N for i in range(M)]
    for i in range(R):
        x, y = map(int, input().split())
        K[x][y] = 1
    
    result = 0
    for i in range(M):
        for j in range(N):
            if dfs(K, i, j) == True:
                result += 1
    print(result)
