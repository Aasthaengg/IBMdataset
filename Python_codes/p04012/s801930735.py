w = list(input())
S = [chr(i) for i in range(97, 97 + 26)]

for S in S:
    if w.count(S) % 2 != 0:
        print("No")
        break
else:
    print("Yes")