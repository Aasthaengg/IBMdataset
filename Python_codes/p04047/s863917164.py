try:
  N = int(input())
  a = map(int, input().split())
  a_ = sorted(a, reverse=True)
  b = []
  for i in range(len(a_)):
      if i%2!=0:
          b.append(a_[i])
  print(sum(b))
except EOFError:
  pass