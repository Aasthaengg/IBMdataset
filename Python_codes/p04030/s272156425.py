import sys
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

s = LS2()
ans = []
for a in s:
    if a != 'B':
        ans.append(a)
    else:
        if len(ans) != 0:
            del ans[-1]

print(''.join(ans))