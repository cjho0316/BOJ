#2667

def dfs(K, x, y):
    global cnt
    if x<=-1 or x>=N or y<=-1 or y>=N:
        return False
    if K[x][y] == 1:
        cnt += 1
        K[x][y] = 0
        dfs(K, x-1, y)
        dfs(K, x, y-1)
        dfs(K, x+1, y)
        dfs(K, x, y+1)
        return True
    return False
    
global cnt

N = int(input())
K, visited = [], []
for i in range(N):
    K.append(list(map(int, input())))

result = 0
for i in range(N):
    for j in range(N):
        cnt = 0
        if dfs(K, i, j) == True:
            visited.append(cnt)
            result += 1

visited.sort()
print(result)
for i in visited:
    print(i)
