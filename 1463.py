#1463

N = int(input())
dp = [0] * 1000001

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    if i%2 == 0 and i%3 ==0:
        dp[i] = min(dp[i], dp[i//3]+1, dp[i//2]+1)
    elif i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    elif i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
print(dp[N])
