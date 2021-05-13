# A - Wanna go back home
def can_go_home(dir1, dir2):
	if dir1 > 0 and dir2 > 0:
		return True
	elif dir1 == 0 and dir2 == 0:
		return True
	else:
		return False


n, w, s, e = 0, 0, 0, 0

for dir in input():
	if dir == 'N':
		n += 1
	elif dir == 'W':
		w += 1
	elif dir == 'S':
		s += 1
	else:
		e += 1

if can_go_home(n, s) and can_go_home(e, w):
	print('Yes')
else:
	print('No')