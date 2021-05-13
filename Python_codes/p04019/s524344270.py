N = input()
NS = set(N)
if len(N) == 1 or len(NS) == 1:
    print("No")
elif "N" not in N and "S" not in N or "W" not in N and "E" not in N :
    print("Yes")
elif "N" in N and "W" in N and "E" in N and "S" in N:
    print("Yes")
else:
    print("No")