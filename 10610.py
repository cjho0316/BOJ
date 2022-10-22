#10610
x = 0
cnt = 0
S = list(str(input()))
S.sort(reverse=True)
S = list(map(int, S))
if sum(S) % 3 != 0 or S[len(S) - 1] != 0:
    print(-1)
else:
    for i in S: 
        print(i, end='')
