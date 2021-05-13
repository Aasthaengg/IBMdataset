def test(): 
  a,b = map(int,input().split())
  arr = []
  for i in range(a):
    value = input()
    arr.append(value)
  arr = "".join(sorted(arr))
  print(arr)
test()