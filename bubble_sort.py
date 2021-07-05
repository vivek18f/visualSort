from time import sleep

def one(i, j, visObj):
    for x in range(visObj.arrSize):
        if x <= visObj.arrSize-i-1:
            visObj.colArr[x] = "orange"
        if x == j:
            visObj.colArr[x] = "blue"
        if x == j + 1:
            visObj.colArr[x] = "magenta"
        if x > visObj.arrSize - i - 1:
            visObj.colArr[x] = visObj.themeColor
    visObj.drawArr()

def two(i, j, visObj):
    for x in range(visObj.arrSize):
        if x <= visObj.arrSize-i-1:
            visObj.colArr[x] = "orange"
        if x == j:
            visObj.colArr[x] = visObj.bgColor
        if x == j + 1:
            visObj.colArr[x] = visObj.bgColor
    visObj.drawArr()

def three(i, j, visObj):
    for x in range(visObj.arrSize):
        if x <= visObj.arrSize-i-1:
            visObj.colArr[x] = "orange"
        if x == j:
            visObj.colArr[x] = "magenta"
        if x == j + 1:
            visObj.colArr[x] = "blue"
    visObj.drawArr()

def bubbleSort(visObj):
    visObj.disableUI()
    count = 0
    for i in range(visObj.arrSize- 1):
        for j in range(visObj.arrSize-1-i):
            
            #call one
            visObj.root.after(int(count*visObj.delay), one(i, j, visObj))
            count += 1

            if visObj.arr[j] > visObj.arr[j+1]:

                #call two
                visObj.root.after(int(count*visObj.delay), two(i, j, visObj))
                count+= 1

                #swapping
                visObj.arr[j], visObj.arr[j+1] = visObj.arr[j+1], visObj.arr[j]

                #call three
                visObj.root.after(int(count*visObj.delay), three(i, j, visObj))
                count += 1

