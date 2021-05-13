S = input()
A = [0, 0, 0, 0]
for i in range(len(S)):
  if S[i] == "N":
    A[0] = 1
  elif S[i] == "S":
    A[1] = 1
  elif S[i] == "E":
    A[2] = 1
  else:
    A[3] = 1
if A[0] ^ A[1] == A[2] ^ A[3] == 0:
  print("Yes")
else:
  print("No")