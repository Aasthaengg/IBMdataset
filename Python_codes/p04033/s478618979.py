a,b = map(int,input().split(' '))
if a > 0:
    ans = 'Positive'
elif b >= 0:
    ans = 'Zero'
else:
    n = b-a+1
    if n%2 == 0:
        ans = 'Positive'
    else:
        ans = 'Negative'
print(ans)