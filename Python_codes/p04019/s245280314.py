s=input()
ok = True

if s.count('N')*s.count('S')==0 and s.count('N')+s.count('S')!=0:
    ok=False
if s.count('W')*s.count('E')==0 and s.count('W')+s.count('E')!=0:
    ok=False
    
if ok:
    print('Yes')
else:
    print('No')