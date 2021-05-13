a, b = map(int, input().split())

ans = ""
if a < 0 and b > 0:
    ans = "Zero"
elif a > 0:
    ans = "Positive"
else:
    ans = "Positive" if abs(a - b + 1) % 2 == 0 else "Negative"

print(ans)