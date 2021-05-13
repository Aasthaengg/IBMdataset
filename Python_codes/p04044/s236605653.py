first= input()
first = first.split()

N = int(first[0])
L =[]
for i in range(N):
  s = input()
  L.append(s)
  
L.sort()
for i in L:
  print(i,end="")

