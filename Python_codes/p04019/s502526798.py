s = input()
kita, minami = sorted([s.count('N'),s.count('S')])
nisi, higasi = sorted([s.count('W'),s.count('E')])
result = ['No','Yes']
r = 1
if kita==minami or kita*minami > 0:
    r *= 1
else:
    r = 0

if nisi==higasi or nisi*higasi > 0:
    r *= 1
else:
    r = 0
print(result[r])