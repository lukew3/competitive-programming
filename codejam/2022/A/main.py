t = int(input())
for i in range(t):
    print(f"Case #{i+1}:")
    r, c = map(int, input().split())
    print(".." + ("+-" * (c-1)) + "+")
    print(".." + ("|." * (c-1)) + "|")
    for j in range(r*2-1):
        if j%2 == 0:
            print("+-" * c + "+")
        else:
            print("|." * c + "|")

