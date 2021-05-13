import sys
input = sys.stdin.readline

def main():
    I = list( map( int , input().split() ) )
    I = sorted( I )
    if I == [5,5,7]:
        print('YES')
    else:
        print('NO')

main()