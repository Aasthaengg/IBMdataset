from sys import stdin
def main():
    #入力
    readline=stdin.readline
    N,M=map(int,readline().split())
    x=[0]*M
    y=[0]*M
    for i in range(M):
        x[i],y[i]=map(int,readline().split())

    box=[1]*(N+1)
    flags=[False]*(N+1)
    flags[1]=True

    for i in range(M):
        out=x[i]
        inn=y[i]
        if flags[out]==True and box[out]==1:
            flags[out]=False
            flags[inn]=True
        elif flags[out]==True:
            flags[inn]=True
        box[out]-=1
        box[inn]+=1

    res=0
    for i in range(N+1):
        if flags[i]==True:
            res+=1
    print(res)
        
if __name__=="__main__":
    main()