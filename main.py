import tkinter
from tkinter import ttk
from tkinter.messagebox import askyesno


# Create the main application window and configure its size and title
root = tkinter.Tk()
root.title("title")
root.geometry("1200x700+350+150")
root.resizable(False,False)


# Placeholder frame is used before the first page is shown
PlaceHolderFrame = ttk.Frame(root)
PlaceHolderFrame.pack()


global CurrentFrameTracker

CurrentFrameTracker = PlaceHolderFrame


# Shared state for the current order and checkout values
global CurrentOrder

CurrentOrder = {}

TotalPriceVar = tkinter.IntVar(value=0)

TotalPriceLabelText = tkinter.StringVar()

CurrentSelectedCartItem = tkinter.StringVar()

CurrentAddress = tkinter.StringVar()

AddressEntry = None






def CreateUtilityBarGridAndButtons(Frame):

    # Configure the utility bar  at the top of the page
    Frame.rowconfigure(0, weight=0, minsize=40)
    Frame.columnconfigure(0, weight=1)

    UtilityBarFrame = ttk.Frame(Frame)
    UtilityBarFrame.rowconfigure(0, weight=1)
    UtilityBarFrame.grid(row=0, column=0, sticky="nsew")


    # Create three cells in the utility bar for button placement
    for column in range(3):

        UtilityBarFrame.columnconfigure(column, weight=2)
        ttk.Label(UtilityBarFrame).grid(row=0, column=column, sticky="nsew")

    CreateUtilityBarButtons(UtilityBarFrame)

 

def CreateHomePageGridAndButtons(HomePageFrame):

    # Build the page header and utility buttons
    CreateUtilityBarGridAndButtons(HomePageFrame)


    # Create the restaurant selection row
    HomePageFrame.rowconfigure(1, weight=1)
    RestrauntButtonRow = ttk.Frame(HomePageFrame)
    RestrauntButtonRow.grid(row=1, column=0, sticky="nsew")
    RestrauntButtonRow.rowconfigure(0, weight=1)


    for column in range(3):
        ttk.Label(RestrauntButtonRow, borderwidth=2, relief="solid").grid(row=0, column=column, sticky="nsew")
        RestrauntButtonRow.columnconfigure(column, weight=1)

    CreateHomePageButtons(RestrauntButtonRow)


def CreateMenuPageGridAndButtons(MenuPageFrame, Elements):


    CreateUtilityBarGridAndButtons(MenuPageFrame)

    MenuPageFrame.rowconfigure(1, weight=1)
    ttk.Label(MenuPageFrame, borderwidth=2, relief="solid").grid(row=1, column=0, sticky="nsew")

    MenuPageFrame.rowconfigure(2, weight=2)
    

    MenuPageRow2Frame = ttk.Frame(MenuPageFrame)
    MenuPageRow2Frame.grid(row=2, column=0, sticky="nsew")
    MenuPageRow2Frame.rowconfigure(0, weight=1)

    for column in range(4):
        MenuPageRow2Frame.columnconfigure(column, weight=1)
        ttk.Label(MenuPageRow2Frame, borderwidth=2, relief="solid").grid(row=0, column=column, sticky="nsew")



    CreateMenuPageButtons(MenuPageFrame, MenuPageRow2Frame, Elements)



def CreateCheckoutFrameGridAndButtons(CheckoutFrame):

    # Build the shared utility bar for the checkout page
    CreateUtilityBarGridAndButtons(CheckoutFrame)

    # Create the row containing the cart view and checkout controls
    CheckoutFrame.rowconfigure(1, weight=1)
    
    CheckoutFrameRow = ttk.Frame(CheckoutFrame)
    CheckoutFrameRow.grid(row=1, column=0, sticky="nsew")
    CheckoutFrameRow.rowconfigure(0, weight=1)

    for column in range(2):
        CheckoutFrameRow.columnconfigure(column, weight=1)
        
    # Create the right panel with checkout controls
    CheckoutWidgetsFrame = ttk.Frame(CheckoutFrameRow)
    CheckoutWidgetsFrame.grid(row=0, column=1, sticky="nsew")
    CheckoutWidgetsFrame.columnconfigure(0, weight=1)

    for row in range(3):
        CheckoutWidgetsFrame.rowconfigure(row, weight=1)


    # Create the address entry panel inside the checkout controls
    AddressEntryFrame = ttk.Frame(CheckoutWidgetsFrame)
    AddressEntryFrame.grid(row=1, column=0, sticky="nsew")
    AddressEntryFrame.rowconfigure(0, weight=1)

    for column in range(2):
        AddressEntryFrame.columnconfigure(column, weight=1)
        

    # Create the left panel containing the cart treeview
    CartTreeviewFrame = ttk.Frame(CheckoutFrameRow)
    CartTreeviewFrame.grid(row=0, column=0, sticky="nsew")
    CartTreeviewFrame.columnconfigure(0, weight=1)

    for row in range(2):
        CartTreeviewFrame.rowconfigure(row, weight=1)


    CartTreeviewWidgetFrame = ttk.Frame(CartTreeviewFrame)
    CartTreeviewWidgetFrame.grid(row=1, column=0, sticky="nsew")
    CartTreeviewWidgetFrame.columnconfigure(0, weight=1)

    for column in range(3):
        CartTreeviewWidgetFrame.columnconfigure(column, weight=1)
    


    CreateCheckoutButtons(CheckoutWidgetsFrame, CartTreeviewWidgetFrame, AddressEntryFrame)
    CreateCartTreeview(CartTreeviewFrame)





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

    HiSushiHomePageImage = tkinter.PhotoImage(file="./Assets/HiSushiHomePage.png")
    HeavensPizzaHomePageImage = tkinter.PhotoImage(file="./Assets/HeavensPizzaHomePage.png")
    RailwayHomePageImage = tkinter.PhotoImage(file="./Assets/RailwayHomePage.png")

    RestrauntButtonLeft = ttk.Button(RestrauntButtonRow, image=HiSushiHomePageImage, command=ShowHiSushiMenu)

    RestrauntButtonLeft.grid(column=0, row=0)

    RestrauntButtonLeft.image = HiSushiHomePageImage

    RestrauntButtonMiddle = ttk.Button(RestrauntButtonRow, image=HeavensPizzaHomePageImage, command=ShowHeavensPizzaMenu)

    RestrauntButtonMiddle.grid(column=1,row=0)

    RestrauntButtonMiddle.image = HeavensPizzaHomePageImage

    RestrauntButtonRight = ttk.Button(RestrauntButtonRow, image=RailwayHomePageImage, command=ShowRailwayMenu)

    RestrauntButtonRight.grid(column=2,row=0)

    RestrauntButtonRight.image = RailwayHomePageImage


def CreateMenuPageButtons(MenuPageRow1Frame, MenuPageRow2Frame, Elements):

    # Show the restaurant banner image at the top of the menu
    RestrauntLogoImagePath = list(Elements.items())[0]

    RestrauntLogoImage = tkinter.PhotoImage(file=RestrauntLogoImagePath[1])

    RestrauntLogoImageLabel = ttk.Label(MenuPageRow1Frame, image=RestrauntLogoImage)

    RestrauntLogoImageLabel.grid(column=0, row=1)

    RestrauntLogoImageLabel.image = RestrauntLogoImage


    # Add the first menu item button
    Option1Item, Option1ImagePath = list(Elements.items())[1]

    Option1Image = tkinter.PhotoImage(file=Option1ImagePath)

    Option1 = ttk.Button(MenuPageRow2Frame, image=Option1Image, command=lambda item=Option1Item: ShowPopUp(item, Elements))

    Option1.grid(column=0, row=0)

    Option1.image = Option1Image

    Option1CurrentQuantity = ttk.Label(MenuPageRow2Frame, text=GetItemQuantity(Option1Item))

    Option1CurrentQuantity.grid(column=1, row=0, sticky="s", pady=20)

    Option1CurrentQuantity = ttk.Label(MenuPageRow2Frame, text=GetItemQuantity(Option1Item))

    Option1CurrentQuantity.grid(column=0, row=0, sticky="s", pady=20)

    # Add the second menu item button
    Option2Item, Option2ImagePath = list(Elements.items())[2]

    Option2Image = tkinter.PhotoImage(file=Option2ImagePath)

    Option2 = ttk.Button(MenuPageRow2Frame, image=Option2Image, command=lambda item=Option2Item: ShowPopUp(item, Elements))

    Option2.grid(column=1, row=0)

    Option2.image = Option2Image

    Option2CurrentQuantity = ttk.Label(MenuPageRow2Frame, text=GetItemQuantity(Option2Item))

    Option2CurrentQuantity.grid(column=1, row=0, sticky="s", pady=20)

    # Add the third menu item button
    Option3Item, Option3ImagePath = list(Elements.items())[3]

    Option3Image = tkinter.PhotoImage(file=Option3ImagePath)

    Option3 = ttk.Button(MenuPageRow2Frame, image=Option3Image, command=lambda item=Option3Item: ShowPopUp(item, Elements))

    Option3.grid(column=2, row=0)

    Option3.image = Option3Image

    Option3CurrentQuantity = ttk.Label(MenuPageRow2Frame, text=GetItemQuantity(Option3Item))

    Option3CurrentQuantity.grid(column=2, row=0, sticky="s", pady=20)

    # Add a checkout button to switch to the checkout page
    ToCheckout = ttk.Button(MenuPageRow2Frame, text="Checkout", command=CreateCheckoutPageFrame)

    ToCheckout.grid(column=3, row=0)


def GetItemQuantity(CurrentItem):

    global CurrentOrder

    if CurrentItem not in CurrentOrder:

        return "Quantity: 0"

    else:

        return f"Quantity: {CurrentOrder[CurrentItem]}"
    

def CreateCheckoutButtons(CheckoutWidgetsFrame, CartTreeviewWidgetFrame, AddressEntryFrame):

    global CurrentOrder, AddressEntry

    # Display the current total at the top of the checkout controls
    TotalLable = ttk.Label(CheckoutWidgetsFrame, textvariable=TotalPriceLabelText)
    TotalLable.grid(column=0, row=0)

    # Create the address input field used for payment delivery
    AddressLabel = ttk.Label(AddressEntryFrame, text="Address:")
    AddressLabel.grid(column=0, row=0, sticky="e")

    AddressEntry = ttk.Entry(AddressEntryFrame)
    AddressEntry.grid(column=1, row=0, sticky="w")

    PayButton = ttk.Button(CheckoutWidgetsFrame, text="Pay", command=PayConfirmation)
    PayButton.grid(column=0, row=2)

    # Disable the pay button if the cart is empty
    if CurrentOrder == {}:
        PayButton.state(["disabled"])
    else:
        PayButton.state(["!disabled"])

        # Show the selected cart item and cart management buttons
        CurrentSelectedCartItemLabel = ttk.Label(CartTreeviewWidgetFrame, textvariable=CurrentSelectedCartItem, width=20, anchor="center", borderwidth=2, relief="solid")
        CurrentSelectedCartItemLabel.grid(row=0, column=0, sticky="nse")

        CurrentOrderKeys = list(CurrentOrder.keys())
        CurrentSelectedCartItem.set(CurrentOrderKeys[0])

        IteratThroughCartButton = ttk.Button(CartTreeviewWidgetFrame, text="Iterate Through Cart", command=lambda: IterateThroughCart(CurrentOrderKeys))
        IteratThroughCartButton.grid(row=0, column=1, sticky="nsew")

        DeleteSelectedCartItemButton = ttk.Button(CartTreeviewWidgetFrame, text="Delete Selected Item", command=DeleteSelectedCartItem)
        DeleteSelectedCartItemButton.grid(row=0, column=2, sticky="nsew")


def SetCurrentAddress():

    # Validate that the address field contains text before checkout
    if AddressEntry is None:
        return False

    if AddressEntry.get() != "":
        CurrentAddress.set(AddressEntry.get())
        return True
    else:

        PleaseEnterAddressPopUp = tkinter.Toplevel(root)
        PleaseEnterAddressPopUp.geometry("200x100+500+200")
        PleaseEnterAddressPopUp.title("Please Enter Address")

        PleaseEnterAddressLabel = ttk.Label(PleaseEnterAddressPopUp, text="Please enter your address.")
        PleaseEnterAddressLabel.pack(expand=True) 

        PleaseEnterAddressPopUp.after(2000, PleaseEnterAddressPopUp.destroy)  
        return False


def IterateThroughCart(CurrentOrderKeys):

    global CurrentOrder

    MaximumIndex = len(CurrentOrderKeys) - 1

    CurentSelectedCartItemIndex = CurrentOrderKeys.index(CurrentSelectedCartItem.get())

    if CurentSelectedCartItemIndex < MaximumIndex:
        CurrentSelectedCartItem.set(CurrentOrderKeys[CurentSelectedCartItemIndex + 1])
    else:
        CurrentSelectedCartItem.set(CurrentOrderKeys[0])


def DeleteSelectedCartItem():

    global CurrentOrder

    SelectedItem = CurrentSelectedCartItem.get()
    if SelectedItem not in CurrentOrder:
        return

    ConfirmDelete = askyesno(title="Confirmation", message=f"Are you sure you want to delete {SelectedItem} from your cart?")

    if ConfirmDelete == False:
        return

    CurrentOrder.pop(SelectedItem)

    CreateCheckoutPageFrame()


def PayConfirmation():

    ValidAddress = SetCurrentAddress()

    if not ValidAddress:
        return

    ansewer = askyesno(title="Confirmation", message=f"Are you sure you want to pay? Your address is: {CurrentAddress.get()}. This will clear your cart.")

    if ansewer == True:

        CurrentOrder.clear()
        TotalPriceVar.set(0)
        CurrentAddress.set("")

        CreateHomePageFrame()
        CreateThankyouPopUp()
        
def CreateThankyouPopUp():

            
        ThankYouPopUp = tkinter.Toplevel(root)
        ThankYouPopUp.geometry("200x100+500+200")
        ThankYouPopUp.title("Thank You")

        ThankYouLabel = ttk.Label(ThankYouPopUp, text="Thank you for your order!")
        ThankYouLabel.pack(expand=True)

        ThankYouPopUp.after(2000, ThankYouPopUp.destroy)


def CreateCartTreeview(TreeviewFrame):

    CartTree = ttk.Treeview(TreeviewFrame, height=9)
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

    TotalPriceVar.set(0)

    for ItemValuesList in CompleteOrderValues:
        TotalPriceVar.set(TotalPriceVar.get() + ItemValuesList[2])

    TotalPriceLabelText.set(f"Total: ${TotalPriceVar.get()}")



def SortOrderValues():
    global CurrentOrder

    ItemsPriceDict = {"Teriyaki Chicken Sushi": 7, "Salmon Avo Sushi": 6, "Apple Juice": 3, "Pepperoni Pizza": 6, "Hawaiian Pizza": 6, "Orange Juice": 3, "Italian Meatball": 7, "Veggie Special": 6, "Mango Juice": 4}

    CurrentOrderNestedList = [list(item) for item in CurrentOrder.items()]

    for i in CurrentOrderNestedList:

        PriceOfCurrentItem = ItemsPriceDict[i[0]]

        TotalPrice = PriceOfCurrentItem * i[1]

        i.append(TotalPrice)


    return CurrentOrderNestedList



def ShowHiSushiMenu():

    HiSushiElements = {"HiSushiBanner": "./Assets/placeholder.png", "Teriyaki Chicken Sushi": "./Assets/TeriyakiChickenSushi.png", "Salmon Avo Sushi": "./Assets/SalmonAvoSushi.png", "Apple Juice": "./Assets/AppleJuice.png"}

    CreateMenuPageFrame(HiSushiElements)

def ShowHeavensPizzaMenu():

    HeavensPizzaElements = {"HeavensPizzaBanner": "./Assets/placeholder.png", "Pepperoni Pizza": "./Assets/PepperoniPizza.png", "Hawaiian Pizza": "./Assets/HawaiianPizza.png", "Orange Juice": "./Assets/OrangeJuice.png"}

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

def ShowPopUp(CurrentItem, Elements):
    global CurrentOrder

    PopUpWindow = tkinter.Toplevel(root)
    PopUpWindow.geometry("200x150+500+200")
    PopUpWindow.title(CurrentItem)

    PopUpWindow.transient(root)
    PopUpWindow.grab_set()

    CreatePopUpGrid(PopUpWindow)

    ItemQuantityVar = tkinter.IntVar(value=CurrentOrder.get(CurrentItem, 0))


    PlusButton = ttk.Button(PopUpWindow, text="+", command=lambda: IncreaseItemQuantity(ItemQuantityVar))
    PlusButton.grid(row=0, column=2)

    MinusButton = ttk.Button(PopUpWindow, text="-", command=lambda: DecreaseItemQuantity(ItemQuantityVar))
    MinusButton.grid(row=0, column=0)

    QuantityDisplay = ttk.Label(PopUpWindow, textvariable=ItemQuantityVar)
    QuantityDisplay.grid(row=0, column=1)


    SubmitButton = ttk.Button(PopUpWindow, text="Submit", command=lambda: SubmitOrder(PopUpWindow, CurrentItem, ItemQuantityVar, Elements))
    SubmitButton.grid(row=1, column=1)


def IncreaseItemQuantity(QuantityVar):

    CurrentQuantity = QuantityVar.get()
    QuantityVar.set(CurrentQuantity + 1)


def DecreaseItemQuantity(QuantityVar):

    CurrentQuantity = QuantityVar.get()

    if CurrentQuantity > 0:
        QuantityVar.set(CurrentQuantity - 1)


def SubmitOrder(PopUpWindow, CurrentItem, QuantityVar, Elements):
    global CurrentOrder

    CurrentItemQuantity = QuantityVar.get()

    if CurrentItemQuantity == 0:

        ansewer = askyesno(title="Confirmation", message=f"Are you sure you don't want {CurrentItem} on your order?")

        if CurrentItem in CurrentOrder and ansewer == True:
            del CurrentOrder[CurrentItem]
        elif CurrentItemQuantity == 0 and ansewer == False:
            return

    else:
        CurrentOrder[CurrentItem] = CurrentItemQuantity

    print(CurrentOrder)

    UpdateTotalPrice(SortOrderValues())

    PopUpWindow.destroy()

    # Refresh the menu page to update quantities
    CreateMenuPageFrame(Elements)


def CreatePopUpGrid(PopUpWindow):
        
    for column in range(3):
        PopUpWindow.columnconfigure(column, weight=1)


    for row in range(2):
        PopUpWindow.rowconfigure(row, weight=1)



def CreateHomePageFrame():

    global CurrentFrameTracker


    CurrentFrameTracker.pack_forget()

    HomePageFrame = ttk.Frame(root)
    HomePageFrame.pack(fill='both', expand=True)

    CurrentFrameTracker = HomePageFrame


    CreateHomePageGridAndButtons(HomePageFrame)


def CreateMenuPageFrame(Elements):

    global CurrentFrameTracker


    CurrentFrameTracker.pack_forget()

    MenuPageFrame = ttk.Frame(root)
    MenuPageFrame.pack(fill='both', expand=True)

    CurrentFrameTracker = MenuPageFrame


    CreateMenuPageGridAndButtons(MenuPageFrame, Elements)

def CreateCheckoutPageFrame():

    global CurrentFrameTracker


    CurrentFrameTracker.pack_forget()

    CheckoutFrame = ttk.Frame(root)
    CheckoutFrame.pack(fill="both", expand=True)

    CurrentFrameTracker = CheckoutFrame

    CreateCheckoutFrameGridAndButtons(CheckoutFrame)





CreateHomePageFrame()

root.mainloop()







