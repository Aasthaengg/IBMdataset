s = list(input())
x = 0
y = 0

if (s.count("S") > 0 and s.count("N") > 0) or (s.count("S") == 0 and s.count("N") == 0):
    if (s.count("E") > 0 and s.count("W") > 0) or (s.count("E") == 0 and s.count("W") == 0):
        print("Yes")
        exit()
    
print("No")
