#10102

V = int(input())

l = list(str(input()))
if l.count('A') > l.count('B'):
    print('A')
elif l.count('A') < l.count('B'):
    print('B')
else:
    print("Tie")
