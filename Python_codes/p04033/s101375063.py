a,b = map(int, input().split())
res = ''
if 0<a:
    res = 'Positive'
elif a*b < 0:
    res = 'Zero'
else:
    if (b-a)%2==0:
        res = 'Negative'
    else:
        res = 'Positive'
print(res)