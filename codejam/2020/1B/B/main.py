import sys
import math

def findCenter(a, b):
    foundEdge=False
    closestMiss = int(( 10**9 ))
    furthestHit = int(0)
    lastHit = False
    while foundTopEdge == False:
        point = int((closestMiss + furthestHit)/2)
        print(str(point) + " " + str(point))
        s = str(input())
        if s == "CENTER":
            foundTopEdge = True
            break
        elif s == "HIT":
            lastHit = True
            furthestHit = point
        elif s == "MISS":
            lastHit = False
            closestMiss = point
        if closestMiss == (furthestHit + 1):
            foundTopEdge = True
        sys.stdout.flush()

    closestMissB = int(-( 10**9 ))
    furthestHitB = int(0)
    while foundBottomEdge == False:
        point = int((closestMissB + furthestHitB)/2)
        print(str(point) + " " + str(point))
        s = str(input())
        if s == "CENTER":
            foundBottomEdge = True
            break
        elif s == "HIT":
            lastHit = True
            furthestHitB = point
        elif s == "MISS":
            lastHit = False
            closestMissB = point
        if closestMissB == (furthestHitB - 1):
            foundBottomEdge = True
        sys.stdout.flush()


    chordLength = math.sqrt(((furthestHit - furthestHitB)**2)*2)
    diameter = 2*a
    num = (diameter/chordLength)/2
    x1 = furthestHit - num
    y1 = furthestHit + num
    x2 = furthestHitB - num
    y2 = furthestHitB + num
    center1 = str(((x1+x2)/2)) + " " + str(((y1+y2)/2))
    x1 = furthestHit + num
    y1 = furthestHit - num
    x2 = furthestHitB + num
    y2 = furthestHitB - num
    center2 = str(((x1+x2)/2)) + " " + str(((y1+y2)/2))

    print(center1)
    s = str(input())
    sys.stdout.flush()
    if s != "CENTER":
        print(center2)


if __name__ == "__main__":
    t, a, b = map(int, input().split())
    for _ in range(t):
        findCenter(a,b)
