def solve(a, n):
    # Brute force; likely not how it's supposed to be done
    for i in range(n):
        x = 0
        for j in range(0, i):
            x = x^a[j]
        for j in range(i+1, n):
            x = x^a[j]
        if x == a[i]:
            return x

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [int(i) for i in input().split()]
        print(solve(a, n))

main()
