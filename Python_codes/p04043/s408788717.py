def check():
  A = list(map(int, input().split()))
  if A.count(5)!=2 or A.count(7)!=1:
    return 'NO'
  return 'YES'
print(check())