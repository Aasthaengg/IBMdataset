from sys import stdin,stdout

def main():
    line=stdin.readline()
    parts=line.split()
    a=int(parts[0])
    b=int(parts[1])
    c= int(parts[2])
    l=[a,b,c]
    l.sort()
    if l[0]==5 and l[1]==5 and l[2]==7:
        stdout.write("YES")
    else:
        stdout.write("NO")
main()