s = input()
output_s = ""

for i in s:
  if i == "B" and len( output_s) != 0:
    output_s = output_s[0:len( output_s)-1]
  elif i != "B":
    output_s += i
  
print(output_s)