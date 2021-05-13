S = input()

n = S.count('N')
w = S.count('W')
s = S.count('S')
e = S.count('E')

def f(n,s):
  return (n==0 and s==0) or (n>0 and s>0)

b = f(n,s) and f(e,w)

if b:
  print("Yes")
else:
  print("No")





