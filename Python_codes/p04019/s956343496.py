from collections import Counter
S = list(input())
S = Counter(S)
ans = "No"
if len(S) == 4:
    ans = "Yes"
elif len(S) == 2:
    if "N" in S and "S" in S:
        ans = "Yes"
    if "W" in S and "E" in S:
        ans = "Yes"
print(ans)

