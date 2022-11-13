#9506

while True:
    M = []
    N = int(input())
    if N == -1:
        break
    for i in range(1, int(N/2)+1):
        if N % i == 0:
            M.append(i)
    if sum(M) != N:
        print(N, "is NOT perfect.")
    elif sum(M) == N:
        print(N, "=", " + ".join(list(map(str, M))))
