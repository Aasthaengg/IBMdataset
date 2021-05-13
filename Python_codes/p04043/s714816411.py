a = input()
a = [int(i)for i in a.split(" ")]
print("YES" if (a[0] == 5 or a[0] == 7) and (a[1] == 5 or a[1] == 7) and (sum(a) == 17) else "NO")