def solve(n):
    if n % 2 != 0: 
        print(-1)
    else:
        print(0, 0, int(n/2))

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        solve(n)

if __name__ == '__main__':
    main()
