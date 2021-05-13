from collections import Counter

S = list(input())
c = Counter(S)

ans = True

if (c["N"]> 0 and c["S"] == 0) or (c["N"]== 0 and c["S"] > 0) or (c["W"] > 0 and c["E"] == 0) or (c["W"] == 0 and c["E"] > 0):
    ans = False

if ans:
    print("Yes")
else:
    print("No")
