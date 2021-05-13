w = input()
X = [0 for i in range(26)]
for i in range(len(w)):
  X[ord(w[i]) - 97] ^= 1
if sum(X) == 0:
  print("Yes")
else:
  print("No")