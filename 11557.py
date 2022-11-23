#11557

T = int(input())
a, b = [], []
for i in range(T):
    cnt = 0
    N = int(input())
    for j in range(N):
        x, y = str(input()).split()
        a.append(x)
        b.append(y)
        if cnt < int(y):
            cnt = int(y)
            school = j
    print(a[school])
