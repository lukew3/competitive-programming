def main():
    n = int(input())
    l = list(map(int, input().split()))
    a = n
    langs = {}
    for i in range(len(l)):
        lang = str(l[i])
        if lang in langs:
            d = i - langs[lang]
            if d < a:
                a = d
        langs[lang] = i
    print(a)

main()
