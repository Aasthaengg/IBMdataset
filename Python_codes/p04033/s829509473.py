a, b = map(int, input().split())
res = ''
if b >= 0:
    if a <= 0:
        res = 'Zero'
    else:
        res = 'Positive'
else:
    if (b - a) % 2 == 0:
        res = 'Negative'
    else:
        res = 'Positive'
print(res)