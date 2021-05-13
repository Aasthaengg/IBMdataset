def main22():
    strbuf = input("");
    strbufs = strbuf.split();
    buf = [];
    for i in range(2):
        buf.append(int(strbufs[i]));
    strbuf = input("");
    strbufs = strbuf.split();
    buf2 = [];
    for i in range(buf[0]):
        buf2.append(int(strbufs[i]));
    if buf[0] == 2:
        if buf2[0] + buf2[1] >= buf[1]:
            print("Possible");
            print(1);
        else:
            print("Impossible");
    else:
        point = -1;
        for i in range((buf[0] - 1)):
            if buf2[i] + buf2[i+1] >= buf[1]:
                point = i+1;
                break;
        if point == -1:
            print("Impossible");
        else:
            print("Possible");
            if point != 1:
                for i in range(point-1):
                    print(i+1);
            if point != buf[0] - 1:
                for i in range(buf[0]-1,point,-1):
                    print(i);
            print(point);

if __name__ == '__main__':
    main22()