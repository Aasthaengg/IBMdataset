words = input().split()

if (words.count("5") == 2) and (words.count("7") == 1):
    ans = "YES"
else:
    ans = "NO"

print(ans)