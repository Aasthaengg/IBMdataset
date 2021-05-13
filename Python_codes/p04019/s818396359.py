S = str(input())
vertical,side = ['N', 'S'], ['W', 'E']

ans1,ans2 = 0,0

for l in vertical:
  if l in S:
    ans1 += 1
for l in side:
  if l in S:
    ans2 += 1
if ans1 >= 2 and ans2 >= 2:
  print('Yes')
elif ans1 >= 2 and ans2 == 0:
  print('Yes')
elif ans1 == 0 and ans2 >= 2:
  print('Yes')
else:
  print('No')