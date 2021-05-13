h = sorted(list(map(int, input().split())))
if (h[0] == h[1]) and (h[1] != h[2]):
    print("YES")
else:
    print("NO")
