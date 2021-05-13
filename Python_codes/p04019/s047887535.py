S = input()
has_N = "N" in S
has_S = "S" in S
has_E = "E" in S
has_W = "W" in S
reachable_NS = has_N and has_S or not has_N and not has_S
reachable_SW = has_E and has_W or not has_E and not has_W
if reachable_NS and reachable_SW:
    print("Yes")
else:
    print("No")
