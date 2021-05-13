w = list(input())
s = list(set(w))

beautiful = True
for i in range(len(s)):
  if w.count(s[i]) % 2 != 0:
    beautiful = False

print("Yes") if beautiful else print("No")