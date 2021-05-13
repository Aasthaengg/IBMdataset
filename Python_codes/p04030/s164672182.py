#入力
input = input()

text = ''

#操作
for i in range(len(input)):
   if input[i] == '0':
      text = text + '0'
   elif input[i] == '1':
      text = text + '1'
   elif input[i] == 'B':
      if text != '':
         text = text[:-1]

#出力
print(text)