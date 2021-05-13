from sys import stdin, stdout

def main():
    line = stdin.readline()
    parts = line.split()
    parts.sort()

    stdout.write('YES' if int(parts[0])==5 and int(parts[1])==5 and int(parts[2])==7 else 'NO')

main()