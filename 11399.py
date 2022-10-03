#11399

i = 0
N = int(input())
M = list(map(int, input().split()))
M.sort()

K = []
for array in M:
    if i == 0:
        K.append(array)
    else:
        K.append(K[i-1] + array)
    i += 1
print(sum(K))
