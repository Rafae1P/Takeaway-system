import tkinter
from tkinter import ttk 
from tkinter.messagebox import askyesno


root = tkinter.Tk()
root.title("title")
root.geometry("1200x700+350+150")
root.resizable(False,False)


style = ttk.Style()
style.configure("BlueStyle", background="Blue", borderwidth=2, relief="solid" )






PlaceHolderFrame = ttk.Frame(root)
PlaceHolderFrame.pack()


global CurrentQuantityFrameTracker

CurrentQuantityFrameTracker = PlaceHolderFrame

global CurrentOrder

CurrentOrder = {}

ItemQuantityTracker = tkinter.IntVar(value=0)







def CreateUtilityBarGridAndButtons(Frame):

    Frame.rowconfigure(0, weight=0, minsize=40)
    Frame.columnconfigure(0, weight=1)

    UtilityBarFrame = ttk.Frame(Frame)
    UtilityBarFrame.rowconfigure(0, weight=1)
    UtilityBarFrame.grid(row=0, column=0, sticky="nsew")


    for column in range(3):

        UtilityBarFrame.columnconfigure(column, weight=2)
        ttk.Label(UtilityBarFrame,  background="Green", borderwidth=2, relief="solid").grid(row=0, column=column, sticky="nsew")

    CreateUtilityBarButtons(UtilityBarFrame)

 

def CreateHomePageGridAndButtons(HomePageFrame):

    CreateUtilityBarGridAndButtons(HomePageFrame)


    HomePageFrame.rowconfigure(1, weight=1)
    RestrauntButtonRow = ttk.Frame(HomePageFrame)
    RestrauntButtonRow.grid(row=1, column=0, sticky="nsew")
    RestrauntButtonRow.rowconfigure(0, weight=1)


    for column in range(3):
        ttk.Label(RestrauntButtonRow,  background="Blue", borderwidth=2, relief="solid").grid(row=0, column=column, sticky="nsew")
        RestrauntButtonRow.columnconfigure(column, weight=1)

    CreateHomePageButtons(RestrauntButtonRow)


def CreateMenuPageGridAndButtons(MenuPageFrame, Elements):


    CreateUtilityBarGridAndButtons(MenuPageFrame)

    MenuPageFrame.rowconfigure(1, weight=1)
    ttk.Label(MenuPageFrame, background="Red", borderwidth=2, relief="solid").grid(row=1, column=0, sticky="nsew")

    MenuPageFrame.rowconfigure(2, weight=2)
    

    MenuPageRow2Frame = ttk.Frame(MenuPageFrame)
    MenuPageRow2Frame.grid(row=2, column=0, sticky="nsew")
    MenuPageRow2Frame.rowconfigure(0, weight=1)

    for column in range(4):
        MenuPageRow2Frame.columnconfigure(column, weight=1)
        ttk.Label(MenuPageRow2Frame, background="Red", borderwidth=2, relief="solid").grid(row=0, column=column, sticky="nsew")



    CreateMenuPageButtons(MenuPageFrame, MenuPageRow2Frame, Elements)



def CreateCheckoutFrameGridAndButtons(CheckoutFrame):

    CreateUtilityBarGridAndButtons(CheckoutFrame)

    CheckoutFrame.rowconfigure(1, weight=1)
    ttk.Label(CheckoutFrame, background="Pink", borderwidth=2, relief="solid").grid(row=1, column=0, sticky="nsew")

    CheckoutFrameRow = ttk.Frame(CheckoutFrame)
    CheckoutFrameRow.grid(row=1, column=0, sticky="nsew")
    CheckoutFrameRow.rowconfigure(0, weight=1)

    for column in range(2):
        CheckoutFrameRow.columnconfigure(column, weight=1)
        ttk.Label(CheckoutFrameRow, background="Pink", borderwidth=2, relief="solid").grid(row=0, column=column, sticky="nsew")


    CheckoutButtonsFrame = ttk.Frame(CheckoutFrameRow)
    CheckoutButtonsFrame.grid(row=0, column=1, sticky="nsew")
    CheckoutButtonsFrame.columnconfigure(0, weight=1)

    for row in range(3):
        CheckoutButtonsFrame.rowconfigure(row, weight=1)
        ttk.Label(CheckoutButtonsFrame, background="Pink", borderwidth=2, relief="solid").grid(row=row, column=0, sticky="nsew")


    CreateCheckoutButtons(CheckoutButtonsFrame)
    CreateCartTreeview(CheckoutFrameRow)





def CreateUtilityBarButtons(Frame):

    #Creating the exit button
    ExitButton = ttk.Button(Frame, text="Exit", command=ConfirmExit)
    
    #Adding button to grid
    ExitButton.grid(column=0, row=0, sticky="nsw")

    #Creating home page button
    HomePageButton = ttk.Button(Frame, text="Home Page", command=CreateHomePageFrame)

    #Adding home page button to grid
    HomePageButton.grid(column=1, row=0, sticky="nsw")

    #Creating cart button
    CartButton = ttk.Button(Frame, text="Cart", command=CreateCheckoutPageFrame)

    #Adding Cart button to grid
    CartButton.grid(column=2, row=0,sticky="nse")


def CreateHomePageButtons(RestrauntButtonRow):


    PlaceHolderImage = tkinter.PhotoImage(file="./Assets/placeholder.png")

   
    RestrauntButtonLeft = ttk.Button(RestrauntButtonRow, image=PlaceHolderImage, command=ShowHiSushiMenu)

    RestrauntButtonLeft.grid(column=0, row=0)

    RestrauntButtonLeft.image = PlaceHolderImage
    

    RestrauntButtonMiddle = ttk.Button(RestrauntButtonRow, image=PlaceHolderImage, command=ShowHeavensPizzaMenu)

    RestrauntButtonMiddle.grid(column=1,row=0)


    RestrauntButtonRight = ttk.Button(RestrauntButtonRow, image=PlaceHolderImage, command=ShowRailwayMenu)

    RestrauntButtonRight.grid(column=2,row=0)
       


def CreateMenuPageButtons(MenuPageRow1Frame, MenuPageRow2Frame, Elements):

#tkinter.PhotoImage(file=RestrauntLogoImagePath[1])
    
    RestrauntLogoImagePath = list(Elements.items())[0]

    RestrauntLogoImage = tkinter.PhotoImage(file=RestrauntLogoImagePath[1])

    RestrauntLogoImageLabel = ttk.Label(MenuPageRow1Frame, image=RestrauntLogoImage)

    RestrauntLogoImageLabel.grid(column=0, row=1)

    RestrauntLogoImageLabel.image = RestrauntLogoImage


    Option1Item, Option1ImagePath = list(Elements.items())[1]

    Option1 = ttk.Button(MenuPageRow2Frame, text=Option1Item, command=lambda item=Option1Item: ShowPopUp(item))

    Option1.grid(column=0, row=0)

    
    Option2Item, Option2ImagePath = list(Elements.items())[2]

    Option2 = ttk.Button(MenuPageRow2Frame, text=Option2Item, command=lambda item=Option2Item: ShowPopUp(item))

    Option2.grid(column=1, row=0)


    Option3Item, Option3ImagePath = list(Elements.items())[3]

    Option3 = ttk.Button(MenuPageRow2Frame, text=Option3Item, command=lambda item=Option3Item: ShowPopUp(item))

    Option3.grid(column=2, row=0)


    ToCheckout = ttk.Button(MenuPageRow2Frame, text="Checkout", command=CreateCheckoutPageFrame)

    ToCheckout.grid(column=3, row=0)




def CreateCheckoutButtons(CheckoutButtonsFrame):

    TotalLable = ttk.Label(CheckoutButtonsFrame, textvariable=TotaPriceVar.get())
    TotalLable.grid(column=0, row=0)

    AddressEntry = ttk.Entry(CheckoutButtonsFrame)
    AddressEntry.grid(column=0, row=1)

    PayButton = ttk.Button(CheckoutButtonsFrame)
    PayButton.grid(column=0, row=2)

def CreateCartTreeview(CheckoutFrameRow):

    CartTree = ttk.Treeview(CheckoutFrameRow, height=9)
    CartTree.grid(column=0, row=0, sticky="N", pady=100)


#defining columns
    CartTree["columns"] = ["Item", "Quantity", "Total"]

    CartTree.column("#0", width=0, minwidth=0)
    CartTree.column("Item", anchor="center", width=120)
    CartTree.column("Quantity", anchor="center", width=120)
    CartTree.column("Total", anchor="center", width=120)

    CartTree.heading("#0", text="Label", anchor="w")
    CartTree.heading("Item", text="Item", anchor="center")
    CartTree.heading("Quantity", text="Quantity", anchor="center")
    CartTree.heading("Total", text="Total", anchor="center")

    CompleteOrderValues = SortOrderValues()

    iidCounter = 0
    for CurrentItem in CompleteOrderValues:
        CartTree.insert(parent="", index="end", iid=iidCounter, text="Parent", values=CurrentItem)
        iidCounter += 1

    UpdateTotalPrice(CompleteOrderValues)


def UpdateTotalPrice(CompleteOrderValues):

    TotalPriceVar = tkinter.IntVar(value=0)

    for ItemValuesList in CompleteOrderValues:

        for ItemValues in ItemValuesList:

            TotalPriceVar.set(TotalPriceVar.get() + ItemValues[2])




def SortOrderValues():
    global CurrentOrder

    ItemsPriceDict = {"Teriyaki Chicken Sushi": 7, "Salmon Sushi": 6, "Apple Juice": 3, "Pepperoni": 6, "Hawaiian": 6, "Orange Juice": 3, "Italian Meatball": 7, "Veggie Special": 6, "Mango Juice": 4}

    CurrentOrderNestedList = [list(item) for item in CurrentOrder.items()]

    for i in CurrentOrderNestedList:

        PriceOfCurrentItem = ItemsPriceDict[i[0]]

        TotalPrice = PriceOfCurrentItem * i[1]

        i.append(TotalPrice)


    return CurrentOrderNestedList



def ShowHiSushiMenu():

    HiSushiElements = {"HiSushiBanner": "./Assets/placeholder.png", "Teriyaki Chicken Sushi": "./Assets/placeholder.png", "Salmon Sushi": "./Assets/placeholder.png", "Apple Juice": "./Assets/placeholder.png"}

    CreateMenuPageFrame(HiSushiElements)

def ShowHeavensPizzaMenu():

    HeavensPizzaElements = {"HeavensPizzaBanner": "./Assets/placeholder.png", "Pepperoni": "./Assets/placeholder.png", "Hawaiian": "./Assets/placeholder.png", "Orange Juice": "./Assets/placeholder.png"}

    CreateMenuPageFrame(HeavensPizzaElements)

def ShowRailwayMenu():

    RailwayElements = {"RailwayBanner": "./Assets/placeholder.png", "Italian Meatball": "./Assets/placeholder.png", "Veggie Special": "./Assets/placeholder.png", "Mango Juice": "./Assets/placeholder.png"}

    CreateMenuPageFrame(RailwayElements)



#Function to confirm if user wants to exit
def ConfirmExit():

#The askyesno function is called which Creates a pop up with a message and to options and returns True or False
    ansewer = askyesno(title="Confirmation", message="Are you sure you want to exit?")

#Checking if user wants to quit or not
    if ansewer == True:
        root.destroy()

def ShowPopUp(CurrentItem):
    global CurrentOrder

    PopUpWindow = tkinter.Toplevel(root)
    PopUpWindow.geometry("200x150+500+200")
    PopUpWindow.title(CurrentItem)

    PopUpWindow.grab_set()

    CreatePopUpGrid(PopUpWindow)

    item_quantity_var = tkinter.IntVar(value=CurrentOrder.get(CurrentItem, 0))


    PlusButton = ttk.Button(PopUpWindow, text="+", command=lambda: IncreaseItemQuantity(item_quantity_var))
    PlusButton.grid(row=0, column=2)

    MinusButton = ttk.Button(PopUpWindow, text="-", command=lambda: DecreaseItemQuantity(item_quantity_var))
    MinusButton.grid(row=0, column=0)

    QuantityDisplay = ttk.Label(PopUpWindow, textvariable=item_quantity_var)
    QuantityDisplay.grid(row=0, column=1)

    ExitButton = ttk.Button(PopUpWindow, text="Submit", command=lambda: SubmitOrder(PopUpWindow, CurrentItem, item_quantity_var))
    ExitButton.grid(row=1, column=1)


def IncreaseItemQuantity(quantity_var):

    CurrentQuantity = quantity_var.get()
    quantity_var.set(CurrentQuantity + 1)


def DecreaseItemQuantity(quantity_var):

    CurrentQuantity = quantity_var.get()

    if CurrentQuantity > 0:
        quantity_var.set(CurrentQuantity - 1)


def SubmitOrder(PopUpWindow, CurrentItem, quantity_var):
    global CurrentOrder

    CurrentItemQuantity = quantity_var.get()

    CurrentOrder[CurrentItem] = CurrentItemQuantity

    print(CurrentOrder)

    PopUpWindow.destroy()

    



def CreatePopUpGrid(PopUpWindow):
        
    for column in range(3):
        PopUpWindow.columnconfigure(column, weight=1)


    for row in range(2):
        PopUpWindow.rowconfigure(row, weight=1)



def CreateHomePageFrame():

    global CurrentQuantityFrameTracker


    CurrentQuantityFrameTracker.pack_forget()

    HomePageFrame = ttk.Frame(root)
    HomePageFrame.pack(fill='both', expand=True)

    CurrentQuantityFrameTracker = HomePageFrame


    CreateHomePageGridAndButtons(HomePageFrame)


def CreateMenuPageFrame(Elements):

    global CurrentQuantityFrameTracker


    CurrentQuantityFrameTracker.pack_forget()

    MenuPageFrame = ttk.Frame(root)
    MenuPageFrame.pack(fill='both', expand=True)

    CurrentQuantityFrameTracker = MenuPageFrame


    CreateMenuPageGridAndButtons(MenuPageFrame, Elements)

def CreateCheckoutPageFrame():

    global CurrentQuantityFrameTracker


    CurrentQuantityFrameTracker.pack_forget()

    CheckoutFrame = ttk.Frame(root)
    CheckoutFrame.pack(fill="both", expand=True)

    CurrentQuantityFrameTracker = CheckoutFrame

    CreateCheckoutFrameGridAndButtons(CheckoutFrame)





CreateHomePageFrame()

root.mainloop()







