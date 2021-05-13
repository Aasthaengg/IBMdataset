import sys 
input=sys.stdin.readline 
def main():
    n=int(input())
    L=list(map(int,input().split()))
    L.sort() 
    ans=0
    for i in range(n):
        ans+=L[i*2]
    else:
        print(ans)

if __name__=="__main__":
    main()