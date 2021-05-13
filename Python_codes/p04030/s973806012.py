s=input()
out=""
for i in range(len(s)):
  if s[i]=="0":
    out=out+"0"
  elif s[i]=="1":
    out=out+"1"
  elif s[i]=="B":
    if out=="":
      continue
    else:
      out=out[:-1]
print(out)