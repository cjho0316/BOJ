# 11478

# input_init
S = input()
K = set()
for i in range(len(S)):
    for j in range(len(S)):
        if i+j+1 > len(S):
            break
        tmp = S[j:j+i+1]
        K.add(tmp)

print(len(K))
