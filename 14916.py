#14916

coin = [5, 2]
N = int(input())

five_cnt = N // coin[0]
N_rem = N - (five_cnt * coin[0])
two_cnt = N_rem // coin[1]
N_rem = N_rem - (two_cnt * coin[1])

if N_rem == 0:
    print(five_cnt+two_cnt)
else:
    while five_cnt >= 0:
        five_cnt -= 1
        if five_cnt == -1:
            print(-1)
            break
        N_rem = N - five_cnt * coin[0]
        two_cnt = N_rem // coin[1]
        N_rem = N_rem - two_cnt * coin[1]
        if N_rem == 0:
            print(five_cnt+two_cnt)
            break
