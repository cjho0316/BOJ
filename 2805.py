#2805

n, m = map(int, input().split())
s = list(map(int, input().split()))

start, result = 0, 0
end = max(s)

while (start <= end):
    total = 0
    mid = (start + end) // 2
    if mid == 0:
        break
    for i in s:
        if i > mid:
            total += i - mid
    if total >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
            
print(result)
    
