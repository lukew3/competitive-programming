def solve(a):
    # Only way I see it is brute forcing
    pass

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [int(i) for i in input().split()]
        print(solve(a))

main()
