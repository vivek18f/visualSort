from time import sleep

def mergeSort(visObj):
    merge_sort_algo(visObj, 0, visObj.arrSize-1)

def merge_sort_algo(visObj, left, right):
    if left < right:
        mid = left + ((right - left) // 2)
        
        merge_sort_algo(visObj, left, mid)
        merge_sort_algo(visObj, mid+1, right)

        merge(visObj, left, mid, right)

def merge(visObj, left, mid, right):

    lArr = visObj.arr[left : mid + 1]
    rArr = visObj.arr[mid + 1 : right + 1]
    
    #print(lArr)
    #print(rArr)
    
    i = 0
    j = 0
    k = left
    
    #print(i, j, k)

    while i < len(lArr)  and j < len(rArr):
        #modifying color array
        for x in range(visObj.arrSize):
            visObj.colArr[x] = "gray38"
            if x >= left and x <= mid:
                visObj.colArr[x] = "blue"
            if x > mid and x <= right:
                visObj.colArr[x] = "green"
            if x >= left and x < k:
                visObj.colArr[x] = visObj.themeColor
        visObj.drawArr()
        sleep(visObj.delay)

        #modifying color array
        for x in range(visObj.arrSize):
            visObj.colArr[x] = "gray38"
            if x >= left and x <= mid:
                visObj.colArr[x] = "blue"
            if x > mid and x <= right:
                visObj.colArr[x] = "green"
            if x >= left and x < k:
                visObj.colArr[x] = visObj.themeColor
            if x == k:
                visObj.colArr[x] = visObj.bgColor
            # uncomment below to highlight where the k's value is being taken from
            #if lArr[i] < rArr[j]:
                #if x == i + left:
                    #visObj.colArr[x] = "magenta"
            #else:
                #if x == mid + 1 + j:
                    #visObj.colArr[x] = "magenta"
        visObj.drawArr()
        sleep(visObj.delay)

        if lArr[i] < rArr[j]:
            visObj.arr[k] = lArr[i]
            i += 1
            k += 1
        else : 
            visObj.arr[k] = rArr[j]
            j += 1
            k += 1

        #modifying color array
        for x in range(visObj.arrSize):
            visObj.colArr[x] = "gray38"
            if x >= left and x <= mid:
                visObj.colArr[x] = "blue"
            if x > mid and x <= right:
                visObj.colArr[x] = "green"
            if x >= left and x < k:
                visObj.colArr[x] = visObj.themeColor
        visObj.drawArr()
        sleep(visObj.delay)

            
    while i < len(lArr):
        #modifying color array
        for x in range(visObj.arrSize):
            visObj.colArr[x] = "gray38"
            if x >= left and x <= mid:
                visObj.colArr[x] = "blue"
            if x > mid and x <= right:
                visObj.colArr[x] = "green"
            if x >= left and x < k:
                visObj.colArr[x] = visObj.themeColor
        visObj.drawArr()
        sleep(visObj.delay)

        #modifying color array
        for x in range(visObj.arrSize):
            visObj.colArr[x] = "gray38"
            if x >= left and x <= mid:
                visObj.colArr[x] = "blue"
            if x > mid and x <= right:
                visObj.colArr[x] = "green"
            if x >= left and x < k:
                visObj.colArr[x] = visObj.themeColor
            if x == k:
                visObj.colArr[x] = visObj.bgColor
        visObj.drawArr()
        sleep(visObj.delay)

        visObj.arr[k] = lArr[i]
        i += 1
        k += 1

        #modifying color array
        for x in range(visObj.arrSize):
            visObj.colArr[x] = "gray38"
            if x >= left and x <= mid:
                visObj.colArr[x] = "blue"
            if x > mid and x <= right:
                visObj.colArr[x] = "green"
            if x >= left and x < k:
                visObj.colArr[x] = visObj.themeColor
        visObj.drawArr()
        sleep(visObj.delay)
        
    while j < len(rArr):
        #modifying color array
        for x in range(visObj.arrSize):
            visObj.colArr[x] = "gray38"
            if x >= left and x <= mid:
                visObj.colArr[x] = "blue"
            if x > mid and x <= right:
                visObj.colArr[x] = "green"
            if x >= left and x < k:
                visObj.colArr[x] = visObj.themeColor
        visObj.drawArr()
        sleep(visObj.delay)

        #modifying color array
        for x in range(visObj.arrSize):
            visObj.colArr[x] = "gray38"
            if x >= left and x <= mid:
                visObj.colArr[x] = "blue"
            if x > mid and x <= right:
                visObj.colArr[x] = "green"
            if x >= left and x < k:
                visObj.colArr[x] = visObj.themeColor
            if x == k:
                visObj.colArr[x] = visObj.bgColor
        visObj.drawArr()
        sleep(visObj.delay)

        visObj.arr[k] = rArr[j]
        j += 1
        k += 1

        #modifying color array
        for x in range(visObj.arrSize):
            visObj.colArr[x] = "gray38"
            if x >= left and x <= mid:
                visObj.colArr[x] = "blue"
            if x > mid and x <= right:
                visObj.colArr[x] = "green"
            if x >= left and x < k:
                visObj.colArr[x] = visObj.themeColor
        visObj.drawArr()
        sleep(visObj.delay)