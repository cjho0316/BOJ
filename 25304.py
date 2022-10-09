#25304

sum = 0
A = int(input())
N = int(input())
for i in range(N):
    a, one = map(int, input().split())
    sum += a*one
if A == sum:
    print('Yes')
else:
    print('No')
