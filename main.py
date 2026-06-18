import tkinter
from tkinter import ttk 
from tkinter.messagebox import askyesno

root = tkinter.Tk()
root.title("title")
root.geometry("1200x700+350+150")
root.resizable(False,False)


style = ttk.Style()
style.configure("BlueStyle", background="Blue", borderwidth=2, relief="solid" )




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


def CreateMenuPageGridAndButtons(MenuPageFrame):


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



    CreateMenuPageButtons(MenuPageFrame, MenuPageRow2Frame)



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









def CreateUtilityBarButtons(Frame):

    #Creating the exit button
    ExitButton = ttk.Button(Frame, text="Exit", command=ConfirmExit)
    
    #Adding button to grid
    ExitButton.grid(column=0, row=0, sticky="nsw")

    #Creating home page button
    HomePageButton = ttk.Button(Frame, text="Home Page")

    #Adding home page button to grid
    HomePageButton.grid(column=1, row=0, sticky="nsw")

    #Creating cart button
    CartButton = ttk.Button(Frame, text="Cart")

    #Adding Cart button to grid
    CartButton.grid(column=2, row=0,sticky="nse")


def CreateHomePageButtons(RestrauntButtonRow):


    PlaceHolderImage = tkinter.PhotoImage(file="./assets/placeholder.png")

   
    RestrauntButtonLeft = ttk.Button(RestrauntButtonRow, image=PlaceHolderImage)

    RestrauntButtonLeft.grid(column=0, row=0)

    RestrauntButtonLeft.image = PlaceHolderImage
    

    RestrauntButtonMiddle = ttk.Button(RestrauntButtonRow, image=PlaceHolderImage)

    RestrauntButtonMiddle.grid(column=1,row=0)


    RestrauntButtonRight = ttk.Button(RestrauntButtonRow, image=PlaceHolderImage)

    RestrauntButtonRight.grid(column=2,row=0)
       


def CreateMenuPageButtons(MenuPageRow1Frame, MenuPageRow2Frame):

    PlaceHolderImage = tkinter.PhotoImage(file="./assets/placeholder.png")

    RestrauntLogoImage = ttk.Button(MenuPageRow1Frame, image=PlaceHolderImage)

    RestrauntLogoImage.grid(column=0, row=1)

    RestrauntLogoImage.image = PlaceHolderImage


    Option1 = ttk.Button(MenuPageRow2Frame)

    Option1.grid(column=0, row=0)


    Option2 = ttk.Button(MenuPageRow2Frame)

    Option2.grid(column=1, row=0)


    Option3 = ttk.Button(MenuPageRow2Frame)

    Option3.grid(column=2, row=0)


    Option4 = ttk.Button(MenuPageRow2Frame)

    Option4.grid(column=3, row=0)




#Function to confirm if user wants to exit
def ConfirmExit():

#The askyesno function is called which creates a pop up with a message and to options and returns True or False
    ansewer = askyesno(title="Confirmation", message="Are you sure you want to exit?")

#Checking if user wants to qut or not
    if ansewer == True:
        root.destroy()




def CreateHomePageFrame():
    HomePageFrame = ttk.Frame(root)
    HomePageFrame.pack(fill='both', expand=True)

    CreateHomePageGridAndButtons(HomePageFrame)


def CreateMenuPageFrame():
    MenuPageFrame = ttk.Frame(root)
    MenuPageFrame.pack(fill='both', expand=True)

    CreateMenuPageGridAndButtons(MenuPageFrame)

def CreateCheckoutPageFrame():
    CheckoutFrame = ttk.Frame(root)
    CheckoutFrame.pack(fill="both", expand=True)
    CreateCheckoutFrameGridAndButtons(CheckoutFrame)

CreateMenuPageFrame()

root.mainloop()







