n, a = map(int, input().split(" "))
list_x = [int(x) - a for x in input().split(" ")]
counts = [{} for i in range(n + 1)]
counts[0][0] = 1
for i, x in enumerate(list_x):
  for v in counts[i]:
    c = counts[i][v]
    if v not in counts[i + 1]:
      counts[i + 1][v] = 0
    counts[i + 1][v] += c
    if v + x not in counts[i + 1]:
      counts[i + 1][v + x] = 0
    counts[i + 1][v + x] += c
print(counts[n][0] - 1)
