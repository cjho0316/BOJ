#1654

n, m = map(int, input().split())
s = []
for i in range(n):
    s.append(int(input()))

start, result = 0, 0
end = max(s)

while (start <= end):
    total = 0
    mid = (start + end) // 2
    if mid == 0:
        result = 1
        break
    for i in s:
        if i // mid > 0:
            total += i // mid
    if total >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
            
print(result)
    
