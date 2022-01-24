def main():
    n = int(input())
    gg = True
    i = 0
    for _ in range(n):
        v = int(input())
        i+=1
        while i != v:
            print(i)
            i += 1
            gg = False
    if gg:
        print("good job")
main()
