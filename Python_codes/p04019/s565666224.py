S=input()
N=len(S)
x=dict()
for i in range(N):
    s = S[i]
    x[s]=s

if "N" in x:
    if "S" in x:
        pass
    else:
        print("No")
        exit()

if "S" in x:
    if "N" in x:
        pass
    else:
        print("No")
        exit()

if "W" in x:
    if "E" in x:
        pass
    else:
        print("No")
        exit()

if "E" in x:
    if "W" in x:
        pass
    else:
        print("No")
        exit()

print("Yes")