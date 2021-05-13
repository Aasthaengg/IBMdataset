s=input()

out=''
for i in range(len(s)):
  if s[i] != 'B':
    out += s[i]
    continue
  else:
    if len(out):
      out = out[:-1]
      
print(out)