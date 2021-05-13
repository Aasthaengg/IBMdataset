def test():
  x=input()
  x=x.split()
  if x == ['5','5','7']:
    print("YES")
  elif x == ['5','7','5']:
    print("YES")
  elif x == ['7','5','5']:
    print("YES")
  else:
    print("NO")
    
test()