s = input()


def walk(s):
    ls = len(s)
    nc = 0
    sc = 0
    wc = 0
    ec = 0
    l=[]
    for i in range(ls):
        if s[i] == "W":
            wc += 1
            l.append(wc)
        elif s[i] == "E":
            ec += 1
            l.append(ec)
        elif s[i] == "N":
            nc += 1
            l.append(nc)
        else:
            sc += 1
            l.append(sc)
    if (wc>0 and ec==0) or (wc==0 and ec>0) or (nc==0 and sc>0) or (nc>0 and sc==0):
        print("No")
        return
    
    else:
        print("Yes")
        return
walk(s)
