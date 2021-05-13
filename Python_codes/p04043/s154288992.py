a = list(map(int, input().split()))

success_cases = [(a[0], a[1], a[2]), (a[1], a[2], a[0]), (a[2], a[0], a[1])]

for c in success_cases:
    if c == (5,7,5):
        print("YES")
        exit(0)
print("NO")

