import sys
D = input()

if ('N' in D and 'S' not in D) or ('N' not in D and 'S' in D):
  print('No')
  sys.exit()

if ('W' in D and 'E' not in D) or ('W' not in D and 'E' in D):
  print('No')
  sys.exit()

print('Yes')