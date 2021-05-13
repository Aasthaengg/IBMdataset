FirstLine = input()
FirstLine = FirstLine.split()
L1 = []
for i in range(int(FirstLine[0])):
  s = input()
  L1.append(s)
L1.sort()
a = ""
for i in L1:
  a += i
 
print(a)