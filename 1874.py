#1874

N = int(input())
M, L = list(), list()
flag, i = 0, 1

while True:
    k = int(input())
    if i <= k:
        while i <= k:
            L.append(i)
            M.append('+')        
            i += 1
    if L[len(L)-1] == k :
        L.pop()
        M.append('-')
        if len(L) == 0 and i-1 == N:
            flag = 0
            break
    else:
        flag = 1
        break

if flag == 1:
    print('NO')
elif flag == 0:
    print(*M, sep = '\n')
