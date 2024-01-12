import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os

class FileOpener:

    def __init__(self, root):
        self.root = root
        self.files_to_be_modified = []
        self.modified_files = []
        self.replaces_done = 0
        root.withdraw()
        self.menu = tk.Toplevel()
        self.menu.geometry("300x300")
        self.menu.resizable = False, False
        self.folder_button = tk.Button(self.menu, text="Select Folder", command=lambda: self.folderSelect())
        self.folder_button.place(relx=0.5, rely=0.3, anchor='center')
        self.loaded_count = tk.Label(self.menu, text="")
        self.loaded_count.place(relx=0.5, rely=0.4, anchor='center')
        self.convert_button = tk.Button(self.menu, text="Convert Files", command=lambda: self.convertFiles())
        self.replaces_done_count = tk.Label(self.menu, text="")
        self.replaces_done_count.place(relx=0.5, rely=0.6, anchor='center')
        self.files_completed = tk.Label(self.menu, text="")
        self.files_completed.place(relx=0.5, rely=0.7, anchor='center')
        pass

    def __del__(self):  # On destruction of object, the start menu reappears
        self.root.deiconify()

    def folderSelect(self):
        self.files_to_be_modified = []
        folder_selected = filedialog.askdirectory()
        print(folder_selected)
        list_of_files = os.listdir(folder_selected)
        for item in list_of_files:
            if ".txt" in item:
                item.replace("'", "")
                self.files_to_be_modified.append(folder_selected + "/" + item)
        self.loaded_count.configure(text=("Loaded files: " + str(len(self.files_to_be_modified))))
        self.convert_button.place(relx=0.5, rely=0.5, anchor='center')

    def convertFiles(self):
        for file in self.files_to_be_modified:
            try:
                os.mkdir(os.getcwd() + "/output")
            except FileExistsError:
                pass
            new_file_lines = []
            file_name = file.split("/")[-1]
            file_name = file_name[0:-4]
            opened_file = open(file, "r")
            new_file = open("output/" + file_name + "_modified.txt", "w")
            for line in opened_file:
                if "Lychee Web" in line:
                    line = line.replace("Lychee Web", "Guava Net")
                    self.replaces_done += 1
                    self.replaces_done_count.configure(text="Replaces done: " + str(self.replaces_done))
                    self.menu.update()
                new_file.write(line)
            self.modified_files.append(new_file)
            self.files_completed.configure(text="Files Complete: " + str(len(self.modified_files)))
            self.menu.update()
            print(self.modified_files)
            opened_file.close()
            new_file.close()
        os.startfile(os.getcwd() + "/output")

