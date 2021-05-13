apple = list(map(str, input().split()))
print("YES" if apple.count("5") == 2 and apple.count("7") == 1 else "NO")