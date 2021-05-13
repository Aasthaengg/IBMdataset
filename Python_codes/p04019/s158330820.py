s = input()
N = s.count('N')
S = s.count('S')
E = s.count('E')
W = s.count('W')
if ((N >= 1 and S == 0) or (N == 0 and S >= 1) or 
    (E >= 1 and W == 0) or (E == 0 and W >= 1)):
  print('No')
else:
  print('Yes')
