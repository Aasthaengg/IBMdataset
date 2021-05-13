N, A = map(int, input().split())
X = list(map(lambda x: int(x) - A, input().split()))

d = {0: 1}

for cur in X:
  for k, v in list(d.items()):
    d[cur + k] = d.get(cur + k, 0) + v
    
print(d[0]-1)