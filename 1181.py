#1181
#init
N = int(input())
S = set([str(input()) for _ in range(N)])
K = sorted(list(S), key=lambda x: (len(x), x))
#print
for i in K:
    print(i)
