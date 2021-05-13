s=input()
n=len(s)
if s.count('N')!=0 and s.count('S')!=0 and s.count('E')!=0 and s.count('W')!=0:
  print('Yes')
elif s.count('N')!=0 and s.count('S')!=0 and s.count('E')==0 and s.count('W')==0:
  print('Yes')
elif s.count('N')==0 and s.count('S')==0 and s.count('E')!=0 and s.count('W')!=0:
  print('Yes')
else:
  print('No')