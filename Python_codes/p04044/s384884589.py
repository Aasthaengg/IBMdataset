N = list(map(int, input().split()))
dic = []

for ins in range(N[0]):
  dic.append(input())

s = ""
for ins in sorted(dic):
  s += ins

print(s)