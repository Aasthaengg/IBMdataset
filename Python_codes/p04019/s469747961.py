string = input()

c1 = True
c2 = True
c3 = True

if ("W" in string and not("E" in string)) or "E" in string and not("W" in string): c1 = False
    
if ("N" in string and not("S" in string)) or "S" in string and not("N" in string): c2 = False

if "N" in string and "S" in string and "E" in string and "W" in string:
    N = string.count("N")
    S = string.count("S")
    W = string.count("W")
    E = string.count("E")
    if not(N/S == W/E or N/S == E/W): c3 = False
    
if c1 and c2 and c3: print("Yes")
else: print("No")