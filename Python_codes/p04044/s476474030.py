Firstline = input()
Firstline = Firstline.split()

List = []
for i in range(int(Firstline[0])):
  List.append(input())

List.sort()
s = ""
for i in List:
  s += i

print(s)