#1920
def binary_search(arr, tgt, start, end):
    if start > end:
        return -1
    mid = (start+end) // 2
    if arr[mid] == tgt:
        return mid
    elif tgt < arr[mid]:
        return binary_search(arr, tgt, start, mid-1)
    else:
        return binary_search(arr, tgt, mid+1, end)


N = int(input())
S = list(map(int, input().split()))
S.sort()

M = int(input())
K = list(map(int, input().split()))
for i in range(len(K)):
    result = binary_search(S, K[i], 0, N-1)
    if result == -1:
        K[i] = 0
    elif S[result] == K[i]:
        K[i] = 1

for j in K:
    print(j)
