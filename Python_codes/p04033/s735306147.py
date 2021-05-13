import sys

input = sys.stdin.readline

def main():
    ans = 'Positive'
    a, b = map(int, input().split())
    if a <= 0 <= b:
        ans = 'Zero' 
    elif b < 0:
        if abs(a-b)%2 == 0:
            ans = 'Negative'
    
    print(ans)

if __name__ == '__main__':
    main()