s = input()
ans = 'Yes'
cn = 'N' in s
ce = 'E' in s
cw = 'W' in s
cs = 'S' in s
if (cn ^ cs) or (ce ^ cw):
    ans = 'No'
print(ans)