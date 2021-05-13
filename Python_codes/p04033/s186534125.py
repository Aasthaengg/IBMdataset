a, b = list(map(int, input().split()))

if 0 < a:
    ans = 'Positive'
elif b < 0:
    if (b - a + 1) % 2 == 0:
        ans = 'Positive'
    else:
        ans = 'Negative'
else:
    ans = 'Zero'
    
print(ans)