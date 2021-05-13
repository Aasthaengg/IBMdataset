s=input()

if s.count("N")>0 and s.count("S")==0:
    print("No")
    exit()
if s.count("S")>0 and s.count("N")==0:
    print("No")
    exit()
if s.count("W")>0 and s.count("E")==0:
    print("No")
    exit()
if s.count("E")>0 and s.count("W")==0:
    print("No")
    exit()
else:
    print("Yes") 