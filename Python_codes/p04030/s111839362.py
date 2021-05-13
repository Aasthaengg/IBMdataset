S = input()
disp = []
for s in S:
    if s=="B":
        if not disp:
            continue
        else:
            disp.pop()
    else:
        disp.append(s)
print("".join(disp))