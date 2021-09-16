def main():
    numCases = int(input())
    for case in range(numCases):
        n = int(input())
        events = []
        orderList = []
        for j in range(n):
            start, end = map(int, input().split())
            event = [start, end]
            orderList.append("0")
            events.append(event)
        camOpen = -1
        jamOpen = -1
        processed = False
        possible = False
        #process one event per iteration
        while processed == False:
            earliestIndex = -1
            earliest = 1441
            #find event that starts the earliest
            for i in range(len(events)):
                event = events[i]
                start = event[0]
                end = event[1]
                if start <= earliest:
                    earliest = start
                    earliestIndex = i
            #get rid of event from list
            if earliest == 1441:
                possible = True
                processed = True
            elif camOpen <= earliest:
                camOpen = events[earliestIndex][1] #cams open time is end time of event
                events[earliestIndex] = [1441, 1441]
                orderList[earliestIndex] = "C"
            elif jamOpen <= earliest:
                jamOpen = events[earliestIndex][1] #jams open time is end time of event
                events[earliestIndex] = [1441, 1441]
                orderList[earliestIndex] = "J"
            else:
                processed = True
                possible = False
        orderString = ''.join(orderList)
        if possible == False:
            orderString = "IMPOSSIBLE"
        print("Case #" + str(case+1) + ": " + orderString)
main()
