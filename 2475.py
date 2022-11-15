#2475
N = list(map(int, input().split()))
for i in range(len(N)):
    N[i] = N[i]**2
print(sum(N)%10)
