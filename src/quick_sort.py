from time import sleep

def quickSort(visObj):
    quick_sort(visObj, 0, visObj.arrSize - 1)

def quick_sort(visObj, left, right):
    if left < right:
        partitionIdx = partition(visObj, left, right)

        quick_sort(visObj, left, partitionIdx-1)
        quick_sort(visObj, partitionIdx+1, right)

def partition(visObj, left, right):
    i = left
    j = left
    pivot = visObj.arr[right]

    while j < right:
        #modifying color array
        for x in range(visObj.arrSize):
            visObj.colArr[x] = "gray38"
            if x <= right and x >= left:
                visObj.colArr[x] = "orange"
            if x == i:
                visObj.colArr[x] = "green"
            if x == j:
                visObj.colArr[x] = "blue"
            if x == right:
                visObj.colArr[x] = "magenta"
        visObj.drawArr()
        sleep(visObj.delay)            

        if visObj.arr[j] < pivot:
            #modifying color array
            for x in range(visObj.arrSize):
                visObj.colArr[x] = "gray38"
                if x <= right and x >= left:
                    visObj.colArr[x] = "orange"
                if x == i:
                    visObj.colArr[x] = visObj.bgColor
                if x == j:
                    visObj.colArr[x] = visObj.bgColor
                if x == right:
                    visObj.colArr[x] = "magenta"
            visObj.drawArr()
            sleep(visObj.delay)            

            # swapping
            visObj.arr[i], visObj.arr[j] = visObj.arr[j], visObj.arr[i]

            #modifying color array
            for x in range(visObj.arrSize):
                visObj.colArr[x] = "gray38"
                if x <= right and x >= left:
                    visObj.colArr[x] = "orange"
                if x == i:
                    visObj.colArr[x] = "blue"
                if x == j:
                    visObj.colArr[x] = "green"
                if x == right:
                    visObj.colArr[x] = "magenta"
            visObj.drawArr()
            sleep(visObj.delay)            

            i += 1
        j += 1

    #modifying color array
    for x in range(visObj.arrSize):
        visObj.colArr[x] = "gray38"
        if x <= right and x >= left:
            visObj.colArr[x] = "orange"
        if x == i:
            visObj.colArr[x] = "green"
        if x == right:
            visObj.colArr[x] = "magenta"
    visObj.drawArr()
    sleep(visObj.delay)            

    #modifying color array
    for x in range(visObj.arrSize):
        visObj.colArr[x] = "gray38"
        if x <= right and x >= left:
            visObj.colArr[x] = "orange"
        if x == i:
            visObj.colArr[x] = visObj.bgColor
        if x == right:
            visObj.colArr[x] = visObj.bgColor
    visObj.drawArr()
    sleep(visObj.delay)            

    #swapping
    visObj.arr[i], visObj.arr[right] = visObj.arr[right], visObj.arr[i]

    #modifying color array
    for x in range(visObj.arrSize):
        visObj.colArr[x] = "gray38"
        if x <= right and x >= left:
            visObj.colArr[x] = "orange"
        if x == i:
            visObj.colArr[x] = "magenta"
        if x == right:
            visObj.colArr[x] = "green"
    visObj.drawArr()
    sleep(visObj.delay)            

    # partition color array depiction
    for x in range(visObj.arrSize):
        visObj.colArr[x] = "gray38"
        if x >= left and x < i:
            visObj.colArr[x] = "blue"
        if x == i:
            visObj.colArr[x] = "magenta"
        if x <= right and x > i:
            visObj.colArr[x] = "green"
    visObj.drawArr()
    sleep(visObj.delay)            

    return i
