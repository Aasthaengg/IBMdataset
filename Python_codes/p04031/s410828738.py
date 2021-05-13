N = int(input())
b = input().split()
a = list(map((lambda x: int(x)), b))

_max = max(a)
_min = min(a)
result = 20000 * N

for i in range(_min,_max+1,1):
  _result = 0
  for j in a:
    _result += (i - int(j))**2
  if _result <= result:
    result = _result
print(result)