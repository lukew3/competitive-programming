def main():
    n = int(input())
    av = [] #allvals
    for i in range(n):
        av.append(list(map(int, input().split())))
    av = sorted(av)
    gi = 0 # greatest index to start checking at
    for i in range(n):
        for j in range(gi, i):
            if j[0] <= 


    print(av)

main()
