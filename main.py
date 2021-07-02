import tkinter as tk 
from PIL import ImageTk, Image
from random import randrange
from time import sleep

from bubble_sort import bubbleSort
from insertion_sort import insertionSort
from merge_sort import mergeSort
from quick_sort import quickSort
from heap_sort import heapSort

class Visualizer:
    def __init__(self):
        # main window
        self.root = tk.Tk() #declaring window and naming it as root
        self.root.title("viSort")
        self.root.geometry("1000x600") #setting window size
        self.root.iconbitmap( "./img/barIcon.ico")
        self.root.resizable(0, 0)

        #variables for gui
        self.bgColor = "black"
        self.borderWidth = 5
        self.reliefStyle = tk.SUNKEN
        self.relPos = "nw"
        self.canvasH = 380
        self.canvasW = 800
        self.themeColor = "cyan"
        self.isDark = True
        
        self.frm2 = None
        self.frm3 = None
        self.speedScale = None
        self.sizeScale = None

        self.themeBtn = None
        self.imgOn = ImageTk.PhotoImage(Image.open("./img/toggleOn.png").resize( (40, 40) ))

        self.imgOff = ImageTk.PhotoImage(Image.open("./img/toggleOff.png").resize( (40, 40) ))

        self.img = self.imgOn

        #variables for sorting
        self.arrSize = 10
        self.arr = []
        self.colArr =[] 
        self.delay = 0.1

        #calling ui functions
        self.titleFrame()
        self.arrayGenFrame()
        self.sortBtnFrame() 
        self.canvas = self.createCanvas()
        self.generateArr()
    
    # ----------------------- UTILITY FUNCTIONS -------------------------------
    def generateArr(self):            
        self.delay = float(self.speedScale.get())
        self.arrSize = int(self.sizeScale.get())

        self.arr = [0] * self.arrSize
        self.colArr = [""] * self.arrSize
        for i in range(self.arrSize):
            self.arr[i] = (randrange(5, self.canvasH + 1))
            self.colArr[i] = "gray38"
        
        self.drawArr()

    def drawArr(self):
        #clear canvas first
        self.canvas.delete("all")

        offset = 13
        spacing = 5
        remainWidth = self.canvasW - offset - ((self.arrSize - 1) * spacing)
        #print(remainWidth)
        barWidth = remainWidth / self.arrSize 
        #print(barWidth)

        normalizedArr = [0] * self.arrSize
        for i in range(self.arrSize):
            if max(self.arr) == 0:
                normalizedArr[i] = self.arr[i] / 1
            normalizedArr[i] = self.arr[i] / max(self.arr)

        for i, height in enumerate(normalizedArr):
            #top left
            x0 = (i * barWidth) + (i * spacing) + offset
            y0 = self.canvasH - height * 340
            #bottom right
            x1 = ((i + 1) * barWidth) + (i * spacing) + offset
            y1 = self.canvasH

            #print(x0, x1)

            self.canvas.create_rectangle(x0, y0, x1, y1, fill=self.colArr[i], outline=self.bgColor)

        self.root.update_idletasks()

    def arrWithTheme(self):
        for i in range(self.arrSize):
            self.colArr[i] = self.themeColor

        self.drawArr()

    def toggleTheme(self):
        if self.isDark:
            self.isDark = False
            self.themeColor = "#e92c2c"
            self.bgColor = "#e8e8e8"
            self.img = self.imgOff

            self.titleFrame()
            self.arrayGenFrame()
            self.sortBtnFrame()
            self.canvas = self.createCanvas()
            for i in range(self.arrSize):
                if self.colArr[i] != "gray38":
                    self.arrWithTheme()
                    break
            self.drawArr()
        else:
            self.isDark = True
            self.themeColor = "cyan"
            self.bgColor = "black"
            self.img = self.imgOn

            self.titleFrame()
            self.arrayGenFrame()
            self.sortBtnFrame()
            self.canvas = self.createCanvas()
            for i in range(self.arrSize):
                if self.colArr[i] != "gray38":                        
                    self.arrWithTheme()
                    break
            self.drawArr()

    def enableUI(self):
        for child in self.frm2.winfo_children():
            child.configure(state="normal")
        for child in self.frm3.winfo_children():
            child.configure(state="normal")

    def disableUI(self):
        for child in self.frm2.winfo_children():
            child.configure(state="disable")
        for child in self.frm3.winfo_children():
            child.configure(state="disable")

    def callBubbleS(self):
        self.delay = float(self.speedScale.get())
        self.disableUI()
        bubbleSort(self)
        self.arrWithTheme()
        self.enableUI()

    def callInsertionS(self):
        self.delay = float(self.speedScale.get())
        self.disableUI()
        insertionSort(self)
        self.arrWithTheme()
        self.enableUI()
        
    def callHeapS(self):
        self.delay = float(self.speedScale.get())
        self.disableUI()
        heapSort(self)
        self.arrWithTheme()
        self.enableUI()

    def callMergeS(self):
        self.delay = float(self.speedScale.get())
        self.disableUI()
        mergeSort(self)
        self.arrWithTheme()
        self.enableUI()

    def callQuickS(self):
        self.delay = float(self.speedScale.get())
        self.disableUI()
        quickSort(self)
        self.arrWithTheme()
        self.enableUI()

    # ----------------------- UI FUNCTIONS -------------------------------
    def titleFrame(self):
        #frame to contain title
        frm1 = tk.Frame(self.root, width=1000, height=40, bg=self.bgColor, relief=self.reliefStyle, bd=self.borderWidth)
        frm1.grid(row=0, column=0, columnspan=2, sticky=self.relPos)
        frm1.pack_propagate(0) #not to change it's size based on widgets it contains i.e. fix it's size

        #title label
        titleLbl = tk.Label(frm1, text="S O R T I N G      V I S U A L I Z E R", fg=self.themeColor, bg=self.bgColor, font=("Arial", 14))
        titleLbl.pack()

    def sortBtnFrame(self):
        #frame to contain all sort buttons
        self.frm2 = tk.Frame(self.root, bg=self.bgColor, width=176, height=560, bd=5, relief=tk.SUNKEN)
        self.frm2.grid(row=1, column=0, rowspan=2, sticky=self.relPos)
        self.frm2.grid_propagate(0)

        #button variables
        btnPadx = 10
        btnPady = 40
        btnWidth = 20
        btnColor = self.themeColor

        #sort buttons defined
        tk.Button(self.frm2, text="Bubble Sort", bg=btnColor, width=btnWidth, command=self.callBubbleS).grid(row=0, padx=btnPadx, pady=btnPady)
        tk.Button(self.frm2, text="Insertion Sort", bg=btnColor, width=btnWidth, command=self.callInsertionS).grid(row=1, padx=btnPadx, pady=btnPady)
        tk.Button(self.frm2, text="Heap Sort", bg=btnColor, width=btnWidth, command=self.callHeapS).grid(row=2, padx=btnPadx, pady=btnPady)
        tk.Button(self.frm2, text="Merge Sort", bg=btnColor, width=btnWidth, command=self.callMergeS).grid(row=3, padx=btnPadx, pady=btnPady)
        tk.Button(self.frm2, text="Quick Sort", bg=btnColor, width=btnWidth, command=self.callQuickS).grid(row=4, padx=btnPadx, pady=btnPady)

    def arrayGenFrame(self):
        #frame to contain sliders and new array button
        self.frm3 = tk.Frame(self.root, width=824, height=156, bg=self.bgColor, bd=self.borderWidth, relief=self.reliefStyle)
        self.frm3.grid(row=1, column=1, sticky=self.relPos)
        self.frm3.grid_propagate(0)

        #variables for scale widgets
        padX = 20
        padY = 40
        borderWidth = 2
        colr = self.themeColor

        #speed slider widget    
        self.speedScale = tk.Scale(self.frm3, from_=0.0, to=2.0, resolution=0.01, digits=3, length=250, orient=tk.HORIZONTAL, label="Delay (in s) :", bd=borderWidth)
        self.speedScale.grid(row=0, column=0, rowspan=2, padx=padX, pady=padY)
        self.speedScale.config(bg=self.bgColor, fg=colr, relief=tk.GROOVE)
        self.speedScale.set(self.delay)

        #array size slider widget
        self.sizeScale = tk.Scale(self.frm3, from_=3, to=50, resolution=1, orient=tk.HORIZONTAL, length=250, label="Array Size :", bd=borderWidth)
        self.sizeScale.grid(row=0, column=1, rowspan=2, padx=padX, pady=padY)
        self.sizeScale.config(bg=self.bgColor, fg=colr, relief=tk.GROOVE)
        self.sizeScale.set(self.arrSize)

        #theme change button
        self.themeBtn = tk.Button(self.frm3, image=self.img, bg=self.bgColor, bd=0, activebackground=self.bgColor, command=self.toggleTheme)
        self.themeBtn.grid(row=0, column=2, sticky="ne")

        #new array button
        tk.Button(self.frm3, text="New Array", bg=colr, width=20, command=self.generateArr).grid(row=1, column=2, padx=padX, pady=0)

        
    def createCanvas(self):  
        #frame to contain canvas          
        frm4 = tk.Frame(self.root, bg=self.bgColor, bd=self.borderWidth, relief=self.reliefStyle)
        frm4.grid(row=2, column=1, sticky=self.relPos)
        
        #canvas for visualizing the sorting
        canvas = tk.Canvas(frm4, bg=self.bgColor, width=self.canvasW, height=self.canvasH, bd=self.borderWidth)
        canvas.grid(row=0, column=0, sticky=self.relPos)
        
        return  canvas

#creating Visualizer class instance and calling the functions
visualizer = Visualizer()

#tkinter main loop
visualizer.root.mainloop()
