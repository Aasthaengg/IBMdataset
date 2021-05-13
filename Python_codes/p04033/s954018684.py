a, b = map(int, input().split())

if a*b < 1:
    ans = "Zero"
elif a > 0:
    ans = "Positive"
else:
    ans = "Positive" if (b-a+1) % 2 == 0 else "Negative"

print(ans)
