a,b = map(int,input().split())

if a < 0 and b >= 0:
    ans = 'Zero'
elif a < 0 and b < 0 and abs(a-b) % 2 == 0:
    ans = 'Negative'
else:
    ans = 'Positive'

print(ans)