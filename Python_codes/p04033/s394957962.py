N = list(map(int,input().split()))
ans = 0
if N [0] < 0 and N[1] > 0:
    ans = "Zero"
elif N[0] < 0:
    if (N[1] - N [0]) % 2 == 0:
        ans = "Negative"
    else:
        ans = "Positive"
elif N[0] > 0:
    ans = "Positive"
else:
    ans = "Zero"

print(ans)
