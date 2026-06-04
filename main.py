import tkinter
from tkinter import ttk 
from tkinter.messagebox import askyesno

root = tkinter.Tk()
root.title("title")
root.geometry("1200x700+350+150")
root.resizable(False,False)


style = ttk.Style()
style.configure("BlueStyle", background="Blue", borderwidth=2, relief="solid" )




def CreateUtilityBarGrid():
    root.rowconfigure(0, weight = 0, minsize=40)
    for column in range(3):
        ttk.Label(root,  background="Blue", borderwidth=2, relief="solid").grid(row=0, column=column, sticky="nsew")
        root.columnconfigure(column, weight=1)

def CreateHomePageGrid():
    root.rowconfigure(1, weight=1)
    for column in range(3):
        ttk.Label(root,  background="Blue", borderwidth=2, relief="solid").grid(row=1, column=column, sticky="nsew")
        root.columnconfigure(column, weight=1)

def CreateUtilityBarButtons():

    #Creating the exit button
    ExitButton = ttk.Button(root, text="Exit", command=ConfirmExit)
    
    #Adding button to grid
    ExitButton.grid(column=0, row=0, sticky="nsw")

    #Creating home page button
    HomePageButton = ttk.Button(root, text="Home Page")

    #Adding home page button to grid
    HomePageButton.grid(column=1, row=0, sticky="nsw")

    #Creating cart button
    CartButton = ttk.Button(root, text="Cart")

    #Adding Cart button to grid
    CartButton.grid(column=2, row=0,sticky="nse")

def CreatRestrauntButtons():

    PlaceHolderImage = tkinter.PhotoImage(file="./assets/placeholder.png")

   
    RestrauntButtonsLeft = ttk.Button(root, image=PlaceHolderImage)

    RestrauntButtonsLeft.grid(column=0, row=1)

    RestrauntButtonsLeft.image = PlaceHolderImage

    RestrauntButtonsMiddle = ttk.Button(root, image=PlaceHolderImage)

    RestrauntButtonsMiddle.grid(column=1,row=1)


    RestrauntButtonsRight = ttk.Button(root, image=PlaceHolderImage)

    RestrauntButtonsRight.grid(column=2,row=1)
       
#Function to confirm if user wants to exit
def ConfirmExit():

#The askyesno function is called which creates a pop up with a message and to options and returns True or False
    ansewer = askyesno(title="Confirmation", message="Are you sure you want to exit?")

#Checking if user wants to qut or not
    if ansewer == True:
        root.destroy()



CreateUtilityBarGrid()
CreateHomePageGrid()
CreateUtilityBarButtons()
CreatRestrauntButtons()


root.mainloop()







