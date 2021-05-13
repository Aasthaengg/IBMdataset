N, L = [int(_) for _ in raw_input().split(" ")]
ret =  [int(_) for _ in raw_input().split(" ")]
index = 0
for i in range(1, len(ret)):
  s = ret[i] + ret[i-1]
  if  L <= s:
    index = i+1
    break

if index == 0:
  print "Impossible"
else:
  print "Possible"
  for i in range(len(ret)-1, index-1, -1):
    print i
  for i in range(1, index):
    print i
