def isPrime(num):
    if num < 3:
        return True
    elif num%2 == 0:
        return False
    else:
        return not ((2**2) % num == 1 or (2**(num-1))%num != 1)

def main():
    s, l = map(int, input().split())
    m = input()
    best = -1
    for i in range(s):
        for j in range(i+1, min(i+l+1, s+1)):
            v = int(m[i:j])
            if v > best and isPrime(v):
                best = v
    if best == -1:
        print("No Primes")
    else:
        print(best)

main()
