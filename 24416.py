#24416

def recursion_fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return (recursion_fib(n-1) + recursion_fib(n-2))
    
def dp_fib(n):
    dp[1] = 1
    dp[2] = 1
    cnt = 0
    for i in range(3, n+1):
        cnt += 1
        dp[i] = dp[i-1] + dp[i-2]
    return cnt
    
N = int(input())
dp = [0] * 10000
print(recursion_fib(N), dp_fib(N))
