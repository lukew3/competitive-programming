import sys

if __name__ == "__main__":
    f = sys.stdin
    T = int(f.readline())
    for _T in range(T):
        X, Y = map(int, f.readline().split())

        def solve(x, y):
            if x == 0 and y == 0:
                return ""
            if (x & 1) + (y & 1) != 1: #if the rightmost digits are both equal to 0 or both equal to 1
                print(x, int(x&1))
                print(y, int(y&1))
                return None
            if abs(x) == 1 and y == 0:
                print("y: " + str(x))
                print("_EW"[x])
                return "_EW"[x]
            if abs(y) == 1 and x == 0:
                print("y: " + str(y))
                print("_NS"[y])
                return "_NS"[y]
            if x & 1: #if movement on x-axis is necessary
                s1 = solve((x - 1) >> 1, y >> 1)
                s2 = solve((x + 1) >> 1, y >> 1)
                if s1 is None and s2 is None:
                    return None
                elif s1 is not None and (s2 is None or len(s2) > len(s1)):
                    return "E" + s1
                else:
                    return "W" + s2
            else: #if movement on y-axis is necessary
                s1 = solve(x >> 1, (y - 1) >> 1)
                s2 = solve(x >> 1, (y + 1) >> 1)
                if s1 is None and s2 is None:
                    return None
                elif s1 is not None and (s2 is None or len(s2) > len(s1)):
                    return "N" + s1
                else:
                    return "S" + s2

        s = solve(X, Y)
        if s is None:
            s = "IMPOSSIBLE"
        print("Case #%d: %s" % (_T + 1, s))
