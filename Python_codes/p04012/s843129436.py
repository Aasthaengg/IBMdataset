import sys
w = list(input())
s = list(set(w))
for i in s:
    if w.count(i) % 2 == 1:
        print("No")
        sys.exit()
print("Yes") 