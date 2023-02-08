#11053

N = int(input())
S = list(map(int, input().split()))
dp = [0] * (N + 1)

for i in range(N):
    for j in range(i):
        if S[i] > S[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
    
print(max(dp))
