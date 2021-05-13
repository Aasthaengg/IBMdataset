a, b = map(int, input().split())
if a <= 0 and 0 <= b:
  print('Zero')
elif a < 0 and b < 0:
  # どっちもマイナス
  print('Positive' if (abs(b - a)) & 1 else "Negative")
else:
  print('Positive')