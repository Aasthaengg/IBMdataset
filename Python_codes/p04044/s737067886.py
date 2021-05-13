import sys
input = sys.stdin.readline

def find_where( List , word ):
    flag = 1
    for i , list_i in enumerate(List):
        if list_i > word:
            flag = 0
            break
    return i + flag

def main():
    n , l = map( int, input().split() )
    I = []
    for i in range(n):
        s = str(input())
        s = s[:-1]
        I.append( s )
    Ss = []
    Ss.append( I[0] )

    for i in range(1,n):
        s = I[i]
        where_i = find_where( Ss , s )


        Ss.insert( where_i , s )

    ans = ''.join(Ss)
    print(ans)

main()