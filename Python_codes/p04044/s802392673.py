def main():
    n,l=map(int,input().split(' '))
    li=[input() for i in range(n)]
    for i in range(n):
        print(min(li),end='')
        li.remove(min(li))

main()
