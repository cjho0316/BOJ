#13023

def dfs(K, v, visited, depth):
    visited[v] = True
    if depth == 4:
        print(1)
        exit()
    for i in K[v]:
        if not visited[i]:
            dfs(K, i, visited, depth+1)
            visited[i] = 0
            # 아니라고 판단했으면 방문표시를 풀어주고 나가기

val = 0
ret = []

N, M = map(int, input().split())
K = [[] for _ in range(N)]
visited = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    K[a].append(b)
    K[b].append(a)

for i in range(M):
    dfs(K, i, visited, 0)
    # dfs를 빠져나왔다는 것은 한번 발 담가보고 아니라고 판단해서 나온것이다.
    # 아니라고 판단했으면 방문표시를 풀어주고 나가기
    visited[i] = 0

print(0)
