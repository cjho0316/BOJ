N = int(input())

for i in range(N):
    M = list(input().split(' '))
    num = float(M[0])
    for j in range(1, len(M)):
        if M[j] == '@':
            num *= 3.0
        elif M[j] == '%':
            num += 5.0
        elif M[j] == '#':
            num -= 7.0
    print(format(num, ".2f"))
