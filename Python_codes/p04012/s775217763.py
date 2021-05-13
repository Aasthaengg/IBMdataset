import collections
w=list(input())
W=collections.Counter(w)
ans="Yes"
for i in W.values():
    if i%2!=0:
        ans="No"
        break

print(ans)