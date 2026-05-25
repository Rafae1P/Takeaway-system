import tkinter
from tkinter import ttk 

root = tkinter.Tk()
root.title("title")
root.geometry("1200x700+350+150")
root.resizable(False,False)


style = ttk.Style()
style.configure("BlueStyle", background="Blue", borderwidth=2, relief="solid" )




def CreateUtilityBarGrid():
    root.rowconfigure(1, weight = 0, minsize=40)
    for column in range(3):
        ttk.Label(root,  background="Blue", borderwidth=2, relief="solid").grid(row=1, column=column, sticky="nsew")
        root.columnconfigure(column, weight=1)

def CreateHomePageGrid():
    root.rowconfigure(2, weight=1)
    for column in range(3):
        ttk.Label(root,  background="Blue", borderwidth=2, relief="solid").grid(row=2, column=column, sticky="nsew")
        root.columnconfigure(column, weight=1)

def CreateUtilityBarButtons():

    #Creating the exit button
    ExitButton = ttk.Button(root, text="Exit", command=lambda: root.quit())
    
    #Adding button to grid
    ExitButton.grid(column=0, row=1, sticky="nsw")

    #Creating home page button
    HomePageButton = ttk.Button(root, text="Home Page")

    #Adding home page button to grid
    HomePageButton.grid(column=1, row=1, sticky="nsw")

    #Creating cart button
    CartButton = ttk.Button(root, text="Cart")

    #Adding Cart button to grid
    CartButton.grid(column=2, row=1,sticky="nse")

CreateUtilityBarGrid()
CreateHomePageGrid()
CreateUtilityBarButtons()
root.mainloop()