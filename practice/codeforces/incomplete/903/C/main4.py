#INCOMPLETE

largenum = 1000000000
boxesCount = int(input())
boxes = input().split()
boxesList = []
for box in boxes:
    boxesList.append(int(box))
emptyList = boxesList
visible = len(emptyList)
filledList = []

boxIsEmpty = False
complete = False
while complete == False:
    tempList = emptyList
    smallest = largenum
    boxIsEmpty = False
    #get smallest box
    for item in emptyList:
        if item < smallest:
            smallest = item
            boxIsEmpty = True
    for item in filledList:
        if item < smallest:
            smallest = item
            boxIsEmpty = False
    #if box is empty remove it from list of possible boxes to put it in
    if boxIsEmpty == True:
        tempList.remove(smallest)
    #find smallest box it can go into
    smallest2 = largenum
    for item in tempList:
        if item > smallest and item < smallest2:
            smallest2 = item
    #conclusion
    if smallest2 != largenum and smallest2 > smallest and boxIsEmpty == False:
        #filledList.append(smallest)
        emptyList.remove(smallest2)
        filledList.append(smallest2)
        visible-=1
    elif smallest2 != largenum and smallest2 > smallest and boxIsEmpty == True:
        #emptyList.remove(smallest)
        emptyList.remove(smallest2)
        filledList.append(smallest2)
        visible-=1
    else:
        complete=True
print(visible)
