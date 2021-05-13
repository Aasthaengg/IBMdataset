N, L = map(int, input().split())
lst = []
for i in range(N):
  lst.append(input())

slst = sorted(lst)
print("".join(slst))