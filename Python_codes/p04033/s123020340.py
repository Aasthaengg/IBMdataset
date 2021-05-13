a, b = map(int, input().split())
if a <= 0 <= b:
    ans = 'Zero'
elif a <= b < 0:
    if (b-a+1) % 2:
        ans = 'Negative'
    else:
        ans = 'Positive'
else:
    ans = "Positive"
print(ans)
