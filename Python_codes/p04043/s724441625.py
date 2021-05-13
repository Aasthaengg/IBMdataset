import itertools
ABC = list(map(str, input().split()))

list_ = list(itertools.permutations(ABC))

if ('5', '7', '5') in list_:
  print('YES')
else:
  print('NO')