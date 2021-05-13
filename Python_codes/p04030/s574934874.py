s=str(input())
edi=[]
for i in s:
  if i=='B' and len(edi)>0:
    edi.pop(-1)
  elif i=='0' or i=='1':
    edi.append(i)
print("".join(edi))