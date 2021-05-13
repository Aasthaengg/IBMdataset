def pair(n,count):
    l=[];su=0
    for i in range(0,len(n),2):
        sub=list()
        sub.append(n[i:i+2])
        su=su+sub[0][0]
        l.append(sub)
    return(su)
        
def ip11(): return int(input())
def ip22(): return [int(_) for _ in input().split()]
        

def main():
    ip1=ip11()
    ip2=ip22()
    ip2.sort()
    print(pair(ip2,ip1))
    return
if __name__ == '__main__':
    main()