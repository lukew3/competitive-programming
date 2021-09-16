
def findRoute(timestart, xstart, ystart, xorg, yorg, path):
    time=timestart
    curx=xstart
    cury=ystart
    pepx=xorg
    pepy=yorg
    if curx != pepx and cury != pepy:
        if time==len(path):
            return -1
        if path[time] == 'N':
            pepy+=1
        elif path[time] == 'S':
            pepy-=1
        elif path[time] == 'E':
            pepx+=1
        elif path[time] == 'W':
            pepx-=1
        time1 = findRoute(time+1, curx+1, cury, pepx, pepy, path)
        time2 = findRoute(time+1, curx-1, cury, pepx, pepy, path)
        time3 = findRoute(time+1, curx, cury+1, pepx, pepy, path)
        time4 = findRoute(time+1, curx, cury-1, pepx, pepy, path)
        print(time1, time2, time3, time4)
        min=100000000000
        if time1>-1 and time1<min:
            min = time1
        if time2>-1 and time2<min:
            min = time2
        if time3>-1 and time3<min:
            min = time3
        if time4>-1 and time4<min:
            min = time4
        return min
    return -1

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        inputLine = str(input()).split()
        x = int(inputLine[0])
        y = int(inputLine[1])
        m = list(inputLine[2])
        #print(x, y, m)
        output = findRoute(0, 0, 0, x, y, m)
        if output == -1:
            output = "IMPOSSIBLE"
        print("Case #" + str(i+1) + ": " + str(output))
