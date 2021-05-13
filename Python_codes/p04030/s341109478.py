s = input()
result = ''
for i in range(0, len(s)):
  if(s[i] == '0'):
  	result = result + '0'
  elif(s[i] == '1'):
    result = result + '1'
  elif(s[i] == 'B'):
    if(len(result) > 0):
    	result = result[ 0 : len(result)-1 ]
print(result)