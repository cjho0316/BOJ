#2579

N = int(input())
L = [0] * (301)
for i in range(N):
    L[i] = int(input())

dp = [0] * (N+2)
dp[0] = L[0]
dp[1] = L[0] + L[1]
dp[2] = max(L[0] + L[2], L[1] + L[2])
for i in range(3, N):
    dp[i] = max(dp[i-2] + L[i], dp[i-3] + L[i] + L[i-1])
print(dp[N-1])
