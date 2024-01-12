import companynamechange as cnc
import noughtsandcrosses as nc
import tkinter as tk
from tkinter import ttk

def createGame():
    noughts_crosses = nc.Game(root)


def nameChange():
    file_opener = cnc.FileOpener(root)


def createMainMenu():
    root = tk.Tk()
    root.title("Python Application")
    noughts_crosses_button = ttk.Button(root, text="Noughts and Crosses", command=lambda: createGame())
    name_change_button = ttk.Button(root, text="Company Name Change", command=lambda: nameChange())
    noughts_crosses_button.grid(row=0, column=0)
    name_change_button.grid(row=1, column=0)
    return root

if __name__ == "__main__":
    root = createMainMenu()
    root.mainloop()
