a, b = map(int, input().split())
res = "Positive"
if b < 0:
    if (b - a + 1) & 1:
        res = "Negative"
elif b >= 0:
    if a <= 0:
        res = "Zero"
print(res)
