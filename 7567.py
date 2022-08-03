#7567
N = list(input())
num = 0

if N[0]:
    num += 10
for i in range(1,len(N)):
    if N[i-1] == N[i]:
        num += 5
    elif N[i-1] != N[i]:
        num += 10
print(num)
