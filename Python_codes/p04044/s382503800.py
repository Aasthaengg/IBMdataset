MM = input().split()
N = int(MM[0])
L = int(MM[1])
list1 = []
for i in range(N):
  a = input()
  list1.append(a)
list1.sort()
for i in list1:
  print(i,end='')