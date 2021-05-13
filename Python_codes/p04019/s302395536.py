if __name__ == '__main__':
    s = input()
    x1 =0
    x2=0
    y1=0
    y2=0

    for i in s:
        if i =="N":
            y1+=1
        if i == "S":
            y2+=1
        if i == "E":
            x1+=1
        if i == "W":
            x2+=1
    if ((x1 ==0 and x2 ==0) or (x1>0 and x2>0) ) and ((y1 ==0 and y2 ==0)or(y1 > 0and y2 > 0)):
        print("Yes")
    else:
        print("No")