t = input()
for i in range(int(t)):
    d, n, k = map(int, input().split())
    rides = []
    for _ in range(n):
        rides.append(list(map(int, input().split())))
    maxscore=0
    for j in range(d):
        dayscore = 0
        ridden = 0
        todays = []
        smallest = 0
        for l in range(len(rides)):
            ride = rides[l]
            if ride[1]-1 < j and ride[2] > j:
                if ridden < k:
                    dayscore += ride[0]
                    ridden+=1
                else:
                    if smallest == -1:
                        smallest = min(todays)[0]
                    if ride[0] > smallest:
                        dayscore -= smallest
                        smallest = -1
                todays.append(ride)
        if dayscore > maxscore:
            maxscore=dayscore
    print(f"Case #{i+1}: {str(maxscore)}")
