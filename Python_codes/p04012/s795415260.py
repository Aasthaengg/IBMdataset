from collections import Counter

w = input()

countAlphabets = Counter(w)
for count in countAlphabets.values():
    if count % 2 != 0:
        print("No")
        exit()

print("Yes")
