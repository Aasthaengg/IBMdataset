def main():
    n = int(input())
    a = list(map(int,input().split()))
    listcost = []
  
    for i in range(min(a),max(a)+1):
        cost = 0
        for j in a:
            if i != j:
                cost += (i - j) ** 2
        listcost.append(cost)
    print(min(listcost))
  
  
if __name__=='__main__':
  main()