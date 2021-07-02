from time import sleep

def heapSort(visObj):
    i = (visObj.arrSize // 2) - 1
    while i >= 0:
        heapify(visObj, visObj.arrSize, i)
        i -= 1
        
    # sorting using heapify i.e. deleting an element of heap and putting it back at the end of array
    j = 0
    n = visObj.arrSize
    
    while j < n:
        #print(visObj.arr)

        #modifying color array
        for x in range(visObj.arrSize):
            visObj.colArr[x] = "orange"
            
            if x > n-j-1:
                visObj.colArr[x] = visObj.themeColor
            if x == 0 or x == n - j - 1:
                visObj.colArr[x] = visObj.bgColor
        visObj.drawArr()
        sleep(visObj.delay)

        #swapping
        visObj.arr[0], visObj.arr[n-j-1] = visObj.arr[n-j-1], visObj.arr[0]

        #modifying color array
        for x in range(visObj.arrSize):
            visObj.colArr[x] = "orange"
            
            if x > n-j-1:
                visObj.colArr[x] = visObj.themeColor
            if x == n - j - 1:
                visObj.colArr[x] = visObj.themeColor
        visObj.drawArr()
        sleep(visObj.delay)
                
        heapify(visObj, n - j -1, 0)
        j += 1
    
    #print(visObj.arr)
    
def heapify(visObj, n, i):
    #parent -- left -- right
    greatest = i # i will denoted by blue color
    left = (i * 2) + 1 # left will denoted by green
    right = (i * 2) + 2 # right will denoted by magenta
    
    #modifying color array
    for x in range(visObj.arrSize):
        visObj.colArr[x] = "orange"
        
        if x == greatest:
            visObj.colArr[x] = "blue"
        if x == left:
            visObj.colArr[x] = "green"
        if x == right:
            visObj.colArr[x] = "magenta"
        if x >= n:
            visObj.colArr[x] = visObj.themeColor
    visObj.drawArr()
    sleep(visObj.delay)

    if left < n and visObj.arr[left] > visObj.arr[greatest]:
        greatest = left
        
    if right < n and visObj.arr[right] > visObj.arr[greatest]:
        greatest = right
        
    if greatest != i:
        
        #modifying color array
        for x in range(visObj.arrSize):
            visObj.colArr[x] = "orange"

            if x == left:
                if left == greatest:
                    visObj.colArr[x] = visObj.bgColor
                else:
                    visObj.colArr[x] = "green"
            if x == right:
                if right == greatest:
                    visObj.colArr[x] = visObj.bgColor
                else:
                    visObj.colArr[x] = "magenta"
            if x == i:
                visObj.colArr[x] = visObj.bgColor
            if x >= n:
                visObj.colArr[x] = visObj.themeColor
        visObj.drawArr()
        sleep(visObj.delay)

        # swapping
        visObj.arr[i], visObj.arr[greatest] = visObj.arr[greatest], visObj.arr[i]

        #modifying color array
        for x in range(visObj.arrSize):

            visObj.colArr[x] = "orange"
            if x == left:
                if left == greatest:
                    visObj.colArr[x] = "blue"
                else:
                    visObj.colArr[x] = "green"
            if x == right:
                if right == greatest:
                    visObj.colArr[x] = "blue"
                else:
                    visObj.colArr[x] = "magenta"
            if x == i:
                if greatest == left:
                    visObj.colArr[x] = "green"
                else:
                    visObj.colArr[x] = "magenta"
            if x >= n:
                visObj.colArr[x] = visObj.themeColor
        visObj.drawArr()
        sleep(visObj.delay)

        # recursion
        heapify(visObj, n, greatest)