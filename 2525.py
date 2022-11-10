#2525
H, M = map(int, input().split())
L = int(input())

num1 = L // 60
num2 = L % 60

H = (H + num1) % 24
if M + num2 > 60:
    H += 1
    if H == 24:
        H = 0
    M = M+num2-60
elif M + num2 == 60:
    H += 1
    if H == 24:
        H = 0
    M = 0
elif M + num2 < 60:
    M = M+num2

print(H, M)
