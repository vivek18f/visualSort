from time import sleep

def insertionSort(visObj):
    for i in range(1, visObj.arrSize):
        j = i
        for x in range(visObj.arrSize):
            visObj.colArr[x] = "orange"
            if x < i:
                visObj.colArr[x] = visObj.themeColor
            if x == j:
                visObj.colArr[x] = "blue"
        visObj.drawArr()
        sleep(visObj.delay)

        currEle = visObj.arr[i]
        while j > 0 and visObj.arr[j-1] > currEle:

            for x in range(visObj.arrSize):
                visObj.colArr[x] = "orange"
                if x < i:
                    visObj.colArr[x] = visObj.themeColor
                if x == j:
                    visObj.colArr[x] = visObj.bgColor
            visObj.drawArr()
            sleep(visObj.delay)

            visObj.arr[j] = visObj.arr[j-1]
            j -= 1

            for x in range(visObj.arrSize):
                visObj.colArr[x] = "orange"
                if x < i:
                    visObj.colArr[x] = visObj.themeColor
                if x == j:
                    visObj.colArr[x] = visObj.bgColor 
            visObj.drawArr()
            sleep(visObj.delay)

        visObj.arr[j] = currEle

        for x in range(visObj.arrSize):
            visObj.colArr[x] = "orange"
            if x < i:
                visObj.colArr[x] = visObj.themeColor
            if x == j:
                visObj.colArr[x] = "blue"
        visObj.drawArr()
        sleep(visObj.delay)

    visObj.arrWithTheme()
