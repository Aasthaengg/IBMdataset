s = input()
ans = True

if 'N' in s and not('S' in s) or 'S' in s and not('N' in s):
    ans = False
if 'E' in s and not('W' in s) or 'W' in s and not('E' in s):
    ans = False
if ans:
    print("Yes")
else:
    print("No")