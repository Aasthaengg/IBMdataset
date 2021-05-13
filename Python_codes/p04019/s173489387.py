S = input()

n = S.count('N')
s = S.count('S')
w = S.count('W')
e = S.count('E')
d = 0
if n > 0:
  d += 1
if s > 0:
  d -= 1
if w > 0:
  d += 2
if e > 0:
  d -= 2
  
if d == 0:
  ans = 'Yes'
else:
  ans = 'No'

print(ans)