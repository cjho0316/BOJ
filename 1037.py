#1037
#init
N = int(input())
S = list(map(int, input().split()))
if N == 1: print(S[0]*S[0])
else: print(max(S)*min(S))
