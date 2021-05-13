from collections import defaultdict
w = input()
d = defaultdict(int)
for c in w:
    d[c] += 1
ans = "Yes"
for v in d.values():
    if v % 2 != 0:
        ans = "No"
        break
print(ans)