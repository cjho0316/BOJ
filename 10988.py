#10988

while True:
    i = 0
    flag = 0
    K = str(input())
    if K == '0': break
    A = list(K)
    N = len(A) - 1
    while i < N:
        if A[i] != A[N]:
            flag = 1
            break
        i += 1
        N -= 1
    if flag == 1:
        print('0')
        break
    elif flag == 0:
        print('1')
        break
