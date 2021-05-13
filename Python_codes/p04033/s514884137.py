a, b = map(int, input().split())


def f(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0


if f(a) == 0 or f(b) == 0:
    ans = "Zero"
elif f(a) == -1 and f(b) == -1:
    diff = b - a
    if (diff + 1) % 2 == 0:
        ans = "Positive"
    else:
        ans = "Negative"
elif f(a) == 1 and f(b) == 1:
    ans = "Positive"
else:
    ans = "Zero"

print(ans)
