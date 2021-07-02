from time import sleep

def bubbleSort(visObj):
    visObj.disableUI()

    for i in range(visObj.arrSize- 1):
        for j in range(visObj.arrSize-1-i):

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
            sleep(visObj.delay)

            if visObj.arr[j] > visObj.arr[j+1]:

                for x in range(visObj.arrSize):
                    if x <= visObj.arrSize-i-1:
                        visObj.colArr[x] = "orange"
                    if x == j:
                        visObj.colArr[x] = visObj.bgColor
                    if x == j + 1:
                        visObj.colArr[x] = visObj.bgColor
                visObj.drawArr()
                sleep(visObj.delay)

                #swapping
                visObj.arr[j], visObj.arr[j+1] = visObj.arr[j+1], visObj.arr[j]

                for x in range(visObj.arrSize):
                    if x <= visObj.arrSize-i-1:
                        visObj.colArr[x] = "orange"
                    if x == j:
                        visObj.colArr[x] = "magenta"
                    if x == j + 1:
                        visObj.colArr[x] = "blue"
                visObj.drawArr()
                sleep(visObj.delay)

