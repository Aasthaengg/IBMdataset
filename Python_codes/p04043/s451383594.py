from sys import stdin, stdout


def main():
    line = stdin.readline()
    parts = line.split()
    a = int(parts[0])
    b = int(parts[1])
    c = int(parts[2])

    count5 = 0
    count7 = 0
    x = 0
    while x < 3:
        if int(parts[x]) == 5:
            count5 += 1
        elif int(parts[x]) == 7:
            count7 += 1
        x += 1

    if count5 == 2 and count7 == 1:
        rta = "YES"
    else:
        rta = "NO"

    stdout.write(rta)



main()