#5597
M = list()
S = [i for i in range(1, 31)]
for i in range (28):
    M.append(int(input()))
M.sort()
K = list(set(S) - set(M))
K.sort()
print(*K , sep='\n')
