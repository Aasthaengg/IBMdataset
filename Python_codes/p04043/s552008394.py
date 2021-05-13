from sys import stdin, stdout


def main():
    line = stdin.readline()
    parts = line.split()
    n = int(parts[0])
    countfive = 0
    countseven = 0
    for i in parts:
        if int(i)==5:
            countfive= countfive+1
        if int(i)==7:
            countseven= countseven+1


    stdout.write( "YES" if countfive==2 and countseven == 1 else "NO")


main()
