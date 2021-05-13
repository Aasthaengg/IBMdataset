n = list(int(i) for i in input().split())

n.sort()

if n[0] == 5 and n[1] == n[0] and n[2] == 7:
    print("YES")
else:
    print("NO")
