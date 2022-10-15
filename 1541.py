#1541

cnt = 0

S = list(map(str, input().split('-')))

for i in range(len(S)):
    if i == 0 and '+' not in S[i]:
        cnt += int(S[i])
    elif '+' in S[i] and i != 0:
        K = list(map(int, S[i].split('+')))
        cnt -= sum(K)
    elif '+' in S[i]:
        K = list(map(int, S[i].split('+')))
        cnt += sum(K)
    else:
        cnt -= int(S[i])

print(cnt)
