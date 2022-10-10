#25305

a, b = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
print(A[b-1])
