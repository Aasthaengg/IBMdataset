a, b, c = (map(int, input().split()))

m = {5: 0, 7: 0}
m[a] = m[a] + 1
m[b] = m[b] + 1
m[c] = m[c] + 1
if m[5] == 2 and m[7] == 1:
    print("YES")
else:
    print("NO")
