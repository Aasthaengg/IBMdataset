ls = [int(s) for s in input().split(" ")]
prels = [[5,7,5],[5,5,7],[7,5,5]]
if ls in prels:
  print("YES")
else :print("NO")