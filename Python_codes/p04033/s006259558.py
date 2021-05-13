from bisect import bisect_right
a, b = (int(x) for x in input().split())
if a <= 0 and 0 <= b: #0を含む
  print('Zero')
elif 0 < a and 0 < b: #すべて正
  print('Positive')
else: #すべて負
  print('Positive' if (b - a + 1)%2 == 0 else 'Negative')
