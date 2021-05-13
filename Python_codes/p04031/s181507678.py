
def main():
    n = int(input())
    a_s = list(map(int,input().split()))
    answer = 999999999999999999999999999999999

    for i in range(-100,101):
        temp = sum([(a-i) ** 2 for a in a_s ])
        answer = min(answer,temp)
    print(answer)

if __name__ == '__main__':
    main()
