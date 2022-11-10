#2525
t = list(map(int, input().split()))
r = int(input())

a = t[0]*3600 + t[1]*60 + t[2] + r

x = a//3600
y = (a - 3600*x)//60
z = a - 3600*x - 60*y
if x >= 24:
    while x >= 24:
        x -= 24

print(x, y, z)
