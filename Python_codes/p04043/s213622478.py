A,B,C = (int(x) for x in input().split())
if A+B+C == 17:
  if A*B*C == 175:
    print ('YES')
  else:
    print ('NO')
else:
  print ('NO')
