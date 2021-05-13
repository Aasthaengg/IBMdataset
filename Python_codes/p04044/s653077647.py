info = input().split()
lst = []
for i in range(int(info[0])):
  lst.append(str(input()))
lst = "".join(sorted(lst))
print((lst))