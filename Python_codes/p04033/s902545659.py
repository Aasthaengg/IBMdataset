a, b = map(int, input().split())
if a*b == 0 or a < 0 < b:
    ans = 'Zero'
elif a > 0 and b > 0:
    ans = 'Positive'
else:
    if (b - a) % 2 == 0:
        ans = 'Negative'
    else:
        ans = 'Positive'

print(ans)