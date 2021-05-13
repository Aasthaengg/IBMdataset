s = input();

st = set(s)
print("Yes" if st == set("WE") or st == set("NS") or st == set("SENW") else "No")