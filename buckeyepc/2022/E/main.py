import math
s, l = map(int, input().split())
m = input()
best = -1
for i in range(s):
    for j in range(i+1, min(i+l+1, s+1)):
        v = int(m[i:j])
        isPrime = True
        for k in range(2, int(math.sqrt(v))+1):
            if v%k == 0:
                isPrime = False
                break
        if isPrime and v > best:
            best = v
if best == -1:
    print("No Primes")
else:
    print(best)
