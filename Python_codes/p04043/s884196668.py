A, B, C = map(int, input().split())
fsf = [A, B, C]
if (fsf.count(5) == 2) & (fsf.count(7) == 1):
    print("YES")
else:
    print("NO")