A, B, C = map(str, input().split())

D = 0
E = 0

if A == "5":
    D =D + 1

if A == "7":
    E =E + 1

if B == "5":
    D =D + 1

if B == "7":
    E =E + 1

if C == "5":
    D =D + 1

if C == "7":
    E =E + 1

if D == 2 and E == 1:
    print("YES")
else:
    print("NO")