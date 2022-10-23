#2587

A = [int(input()) for i in range(5)]
A.sort()
print(int(sum(A) / 5))
print(A[int(len(A)/2)])
