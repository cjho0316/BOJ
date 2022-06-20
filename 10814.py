#10814
#init
N = int(input())
S = [[0]*2 for _ in range(N)]
#append_in_dict
for i in range(N):
    S[i][0],S[i][1] = list(input().split())
    S[i][0] = int(S[i][0])

K = sorted(S, key=lambda x:x[0])
#print
for i in range(len(K)):
    print(K[i][0], K[i][1])
