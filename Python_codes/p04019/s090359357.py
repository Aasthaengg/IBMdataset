s = input()
n_cnt = 0
s_cnt = 0
e_cnt = 0
w_cnt = 0
for i in range(len(s)):
  if s[i] == 'N':
    n_cnt += 1
  if s[i] == 'S':
    s_cnt += 1
  if s[i] == 'W':
    w_cnt += 1
  if s[i] == 'E':
    e_cnt += 1
if (n_cnt > 0 and s_cnt > 0) or (n_cnt == 0 and s_cnt == 0):
  length = True
else:
  length = False
if (e_cnt > 0 and w_cnt > 0) or (e_cnt == 0 and w_cnt == 0):
  width = True
else:
  width = False
  
if length and width:
  print('Yes')
else:
  print('No')