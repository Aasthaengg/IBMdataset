S=input()
ans="Yes"
if "N" in S and not "S" in S:
  ans="No"
if "S" in S and not "N" in S:
  ans="No"
if "E" in S and not "W" in S:
  ans="No"
if "W" in S and not "E" in S:
  ans="No"
print(ans)
