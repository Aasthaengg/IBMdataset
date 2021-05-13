S = input()

n = S.count('N')
s = S.count('S')
w = S.count('W')
e = S.count('E')
a = 0

if n > 0:
    a += 1
if s > 0:
    a -= 1
if w > 0:
    a += 2
if e > 0:
    a -= 2

if a == 0:
    print("Yes")
else:
    print("No")
