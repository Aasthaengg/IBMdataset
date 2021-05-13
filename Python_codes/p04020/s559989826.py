import sys
input = sys.stdin.buffer.readline

def main():
    N = int(input())
    ans = 0
    L = [0]
    for i in range(N):
        num = int(input())
        if L[-1] == 0:
            ans += (num//2)
            L.append(num%2)
        else:
            if num == 0:
                L.append(num)
                continue
            else:
                num -= 1
                ans += (num//2+1)
                L.append(num%2)
                
    print(ans)
            
if __name__ == "__main__":
    main()
