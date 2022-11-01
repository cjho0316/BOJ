#2566

col = 0
row = 0
val = 0
A = [[0]*9 for i in range(9)]
for i in range(9):
    A[i] = list(map(int, input().split()))

for i in range(9):
    for j in range(9):
        if A[i][j] > val:
            col = i
            row = j
            val = A[i][j]
        
print(val)
print(col+1, row+1)
