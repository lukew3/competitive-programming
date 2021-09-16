#https://codeforces.com/problemset/problem/1323/B
def get_all_factors(n):
    factors = []
    for i in range(1,n+1):
        factorSet=[]
        if n%i == 0:
            factorSet.append(i)
            factorSet.append(int(n/i))
            factors.append(factorSet)
    return factors

def makeArray(n, m, a, b):
    c = [ [ None for i in range(m) ] for j in range(n) ]
    print(c)
    for i in range(len(c)):
        for j in range(len(c[0])):
            c[i][j] = a[i] * b[j]
    return c

def countRec(c, k, factors):
    for i in range(len(c)):
        for j in range(len(c[i])):
            maxx = 0
            maxy = 0
            y = i
            x = j
            print("(" + str(x)+", " + str(y)+ ")")
            val = c[i][j]
            print(val)
            if val==0:
                continue
            for factor in factors:
                possible = True
                length = factor[0]
                height = factor[1]
                curPosx = j
                curPosy = i
                while rectLength != length:
                    if c[curPosx][curPosy] == 0:
                        possible=False
                        break
                    rectLength+=1
                while rectHeight != height:
                    if c[curPosx][curPosy] == 0:
                        possible=False
                        break
                    rectHeight+=1
                #print(length)
                #print(height)

    print(factors)
    return 0

if __name__ == "__main__":
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = makeArray(n, m, a, b)
    factors = get_all_factors(k)
    count = countRec(c, k, factors)
    print(c)
    print(count)
