import sys

def solve(m):
    w = 0
    h = 0
    wl = 0 # width of current line
    hl = 0 # height of base of current line
    rw, rh = map(int, input().split())
    while(rw != -1 and rh != -1):
        if wl+rw <= m:
            wl += rw
            if hl + rh > h:
                h = hl + rh
        else:
            if wl > w:
                w = wl
            hl = h
            h += rh
            wl = rw
        rw, rh = map(int, input().split())
    if wl > w:
        w = wl
    print(f'{w} x {h}')
        

def main():
    m = int(input())
    while (m!= 0):
        solve(m)
        m = int(input())
            
main()
