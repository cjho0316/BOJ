# 10156

# input_init
A, B, C = map(int, input().split())

s = A*B-C
if s < 0:
    print(0)
else:
    print(s)
