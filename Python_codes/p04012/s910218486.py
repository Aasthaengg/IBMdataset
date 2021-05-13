w = list(input())
W = set(w)

for i in W:
    ans = w.count(i)
    if ans % 2 == 1:
        print("No")
        exit()
print("Yes")