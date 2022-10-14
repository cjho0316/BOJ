#1439

cnt = 0
x = 0
S = list(str(input()))

for i in range(len(S)):
    if i == 0:
        x = S[i]
    elif S[i] == S[i-1]:
        pass
    elif S[i] != x:
        cnt += 1

print(cnt)
