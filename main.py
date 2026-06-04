import tkinter
from tkinter import ttk 
from tkinter.messagebox import askyesno

root = tkinter.Tk()
root.title("title")
root.geometry("1200x700+350+150")
root.resizable(False,False)


style = ttk.Style()
style.configure("BlueStyle", background="Blue", borderwidth=2, relief="solid" )




def CreateUtilityBarGrid(Frame):

    Frame.rowconfigure(0, weight = 0, minsize=40)
    for column in range(3):
        ttk.Label(Frame,  background="Blue", borderwidth=2, relief="solid").grid(row=0, column=column, sticky="nsew")
        Frame.columnconfigure(column, weight=1)


def CreateHomePageGrid(HomePageFrame):

    CreateUtilityBarGrid(HomePageFrame)

    HomePageFrame.rowconfigure(1, weight=1)

    for column in range(3):
        ttk.Label(HomePageFrame,  background="Blue", borderwidth=2, relief="solid").grid(row=1, column=column, sticky="nsew")
        HomePageFrame.columnconfigure(column, weight=1)


def CrateMenuPageGrid(MenuPageFrame):

    CreateUtilityBarGrid(MenuPageFrame)

    for row in range(4):
        ttk.Label(MenuPageFrame, background="Red",)

    MenuPageFrame.rowconfigure(1, weight=1)





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


def CreatHomePageButtons(HomePageFrame):

    CreateUtilityBarButtons(HomePageFrame)

    PlaceHolderImage = tkinter.PhotoImage(file="./assets/placeholder.png")

   
    RestrauntButtonLeft = ttk.Button(HomePageFrame, image=PlaceHolderImage)

    RestrauntButtonLeft.grid(column=0, row=1)

    RestrauntButtonLeft.image = PlaceHolderImage

    RestrauntButtonMiddle = ttk.Button(HomePageFrame, image=PlaceHolderImage)

    RestrauntButtonMiddle.grid(column=1,row=1)


    RestrauntButtonRight = ttk.Button(HomePageFrame, image=PlaceHolderImage)

    RestrauntButtonRight.grid(column=2,row=1)
       

#Function to confirm if user wants to exit
def ConfirmExit():

#The askyesno function is called which creates a pop up with a message and to options and returns True or False
    ansewer = askyesno(title="Confirmation", message="Are you sure you want to exit?")

#Checking if user wants to qut or not
    if ansewer == True:
        root.destroy()




def CreatHomePageFrame():
    HomePageFrame = ttk.Frame(root)
    HomePageFrame.pack(fill='both', expand=True)

    CreateHomePageGrid(HomePageFrame)
    CreatHomePageButtons(HomePageFrame)


def CreateMenuPageFrame():
    MenuPageFrame = ttk.Frame(root)
    MenuPageFrame.pack(fill='both', expand=True)



root.mainloop()







