S = input()
A = []

for s in S:
  if s=="0" or s=="1":
    A.append(s)
  else:
    A = A[:len(A)-1]
    
print(*A,sep="")