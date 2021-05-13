s = input()

s = list(s)
sowth = s.count('S') if 'S' in s else 0
east  = s.count('E') if 'E' in s else 0
north = s.count('N') if 'N' in s else 0
west  = s.count('W') if 'W' in s else 0

if (west != 0 and east != 0 and sowth == 0 and north == 0) or\
    (sowth != 0 and north != 0 and west == 0 and east == 0) or\
    (sowth != 0 and north != 0 and west != 0 and east != 0):
    print('Yes')
else:
    print('No')
