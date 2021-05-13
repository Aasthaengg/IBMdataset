a, b = map(int, input().split())
list = []
for i in range(a):
  list.append(input())
list1 = sorted(list)
for i in list1:
  print(i, end = "")