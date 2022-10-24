#10162

T = int(input())

A, B, C = 300, 60, 10
a = T // 300
T %= A
b = T // 60
T %= B
c = T // 10
T %= C
if T == 0:
    print(a, b, c)
else:
    print(-1)
