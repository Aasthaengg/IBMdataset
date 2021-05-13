a,b = map(int,input().split())
if 0<a:
    ans = 'Positive'
elif b<0:
    ans = 'Positive' if (b-a)%2==1 else 'Negative'
else:
    ans = 'Zero'
print(ans)