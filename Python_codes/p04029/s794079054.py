n = int(input())
def rec(a):
  if a == 1:
    return 1
  else:
    return a + rec(a - 1)
  
print(rec(n))