import math

def score(a):
    # Return number of too tall piles
    v = 0
    for i in range(1, len(a)-1):
        v += int(a[i] > a[i-1] + a[i+1])
    return v

def solve(n, k, a):
    # max value of m is ceil((n-2)/2)
    if k > 1:
        return score(a)
    else:
        return math.ceil((n - 2) / 2)

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = [int(i) for i in input().split()]
        print(solve(n, k, a))

main()
