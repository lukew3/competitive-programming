def lower(n):
    a = ""
    fp = int(n[0])-1
    while fp > 0:
        if str(fp) not in n:
            a = str(fp)
            break
        fp-=1
    b = ""
    sp = 9
    while sp > -1:
        if str(sp) not in n:
            b = str(sp)
            break
        sp-=1
    if b == '':
        return ''
    return f"{a}{b*(len(n)-1)}"


def upper(n):
    a = ''
    fp = int(n[0])+1
    while fp < 1

def main():
    n = input()
    l = lower(n)
    u = upper(n)
    if l == '':
        print('Impossible')
    else:
        print(l)
    
main()
