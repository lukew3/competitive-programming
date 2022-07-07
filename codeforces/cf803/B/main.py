import math

def score(a):
    # Return number of too tall piles
    v = 0
    for i in range(1, len(a)-1):
        if a[i] > a[i-1] + a[i+1]:
            v += 1
    return v

def solve(n, k, a):
    # max value of m is ceil((n-2)/2)
    return max(score(a), math.ceil((n-2)/2) - k + math.ceil(n/2))

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = [int(i) for i in input().split()]
        print(solve(n, k, a))

main()
