# -*- coding: utf-8 -*-

def main():

    
    N = int(input())
    a = list(map(int, input().split()))

    cost = 0
    listCost = []

    for i in range(min(a), max(a)+1):
        for j in a:
            if i != j:
                cost += (i - j) ** 2

        listCost.append(cost)
        cost = 0

    ans = min(listCost)

    print(ans)
    

if __name__ == "__main__":
    main()