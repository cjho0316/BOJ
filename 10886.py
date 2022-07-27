#10886

N = int(input())
A, B = 0, 0
while(N):
    M = int(input())
    if M == 1:
        A += 1
    elif M == 0:
        B += 1
    N -=1
print("Junhee is cute!" if A > B else "Junhee is not cute!")
