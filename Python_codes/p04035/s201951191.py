def get_ints():
    return list(map(int, input().split()))

[n, l] = get_ints()
a = get_ints()

for i in range(n - 1):
    if a[i] + a[i + 1] < l:
        continue
    print("Possible")
    for j in range(1, i + 1):
        print(j)
    for j in range(n - 1, i, -1):
        print(j)
    exit(0)

print("Impossible")
