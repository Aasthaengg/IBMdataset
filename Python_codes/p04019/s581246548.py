t = input()

n = False
s = False
e = False
w = False

for i in range(len(t)):
    n = n or t[i] == 'N'
    s = s or t[i] == 'S'
    e = e or t[i] == 'E'
    w = w or t[i] == 'W'

ok = True
ok = (n and s) or (not n and not s)
ok = ok and ((e and w) or (not e and not w))
print('Yes' if ok else 'No')
