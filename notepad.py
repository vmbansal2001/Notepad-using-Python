from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])

        if file == "":
            file = None

        else:
            #Save as new File
            f = open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()

        root.title(os.path.basename(file) + " - Notepad")
        print("File Saved")

    else:
        f = open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()

def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad","Notepad by Vipul Bansal")



if __name__ == "__main__":
    root = Tk()
    root.title("Untitled - Notebook")
    root.geometry("644x788")

    #Text Area
    TextArea = Text(root)
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    #Menu Bar
    MenuBar = Menu(root)

    #File Menu
    FileMenu = Menu(MenuBar, tearoff=0)
    #For new File
    FileMenu.add_command(label="New", command=newFile)
    #To open existing File
    FileMenu.add_command(label="Open", command=openFile)
    #To save the current File
    FileMenu.add_command(label="Save", command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quitApp)
    MenuBar.add_cascade(label="File", menu=FileMenu)
    

    #Edit Menu
    EditMenu = Menu(MenuBar, tearoff=0)
    #Cut
    EditMenu.add_command(label="Cut", command=cut)
    #Copy
    EditMenu.add_command(label="Copy", command=copy)
    #Paste
    EditMenu.add_command(label="Paste", command=paste)
    MenuBar.add_cascade(label="Edit", menu=EditMenu)

    #Help Menu
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="About Notepad", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    root.config(menu=MenuBar)

    #Adding Scrollbar
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)


    root.mainloop()