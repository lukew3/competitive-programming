n = int(input())
d = {
    0 : 6,
    1 : 1,
    2 : 2,
    3 : 3,
    4 : 4,
    5 : 5,
    6 : 5,
    7 : 6,
    8 : 6,
    9 : 6,
}
def func(n):
    if n in d:
        return d[n]
    if str(n)[0] == 0:
        return 100000
    x = n
    if not n % 10:
        x = min(x, func(n - 1) + 1)

    if not n % 11 and n > 11:
        x = min(x,  2 + func(n // 11))

    if not n % 111 and n > 111:
        x = min(x, 3 + func(n // 111))

    if not n % 11111 and n > 11111:
        x = min(x, 5 + func(n // 11111))

    s = str(n)
    # x = min(x, sum([func(int(i)) for i in s]))
    # for i in s:
    #     x = min(x, func(int(i)))
    for i in range(1, len(str(n))):
        x = min(x, func(int(s[:i])) + func(int(s[i:])))

    return x

# for i in range(1, 1001):
#     print(i, ":", func(i))

print(func(n))