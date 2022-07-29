# Python:   3.9.7
#
# Author:   Samantha
#
# Purpose:  To create a program to move files from one folder to another.


import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil

class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self)
        self.master.title("File Transfer") # sets the title
        #creates button to select files
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        #button position
        self.sourceDir_btn.grid(row=0, column=0, padx=(20,10), pady=(30,0))

        #creates entry for source directory selection
        self.source_dir = Entry(width=75)
        #entry position, same padding as button so they line up correctly
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20,10), pady=(30,0))

        #creates button to select destination
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        #button position, under source button
        self.destDir_btn.grid(row=1, column=0, padx=(20,10), pady=(15,10))

        #creates entry for destination directory selection
        self.destination_dir = Entry(width=75)
        #entry position, same padding as button so they line up correctly
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20,10), pady=(15,10))

        #creates button to transfer files
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        #positions file transfer button
        self.transfer_btn.grid(row=2, column=1, padx=(200,0), pady=(0,15))

        #creates exit button
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        #positions exit button
        self.exit_btn.grid(row=2, column=2, padx=(10,40), pady=(0,15))
        
    #creates function to select source directory
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #.delete(0,END) will clear the entry widget content of previous text/entry
        self.source_dir.delete(0,END)
        #.insert will insert the users selection to the source_dir entry
        self.source_dir.insert(0, selectSourceDir)

    #creates function to select destination directory
    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        self.destination_dir.delete(0,END)
        self.destination_dir.insert(0, selectDestDir)

    #creates function to transfer files from one directory to another
    def transferFiles(self):
        #gets source directory
        source = self.source_dir.get()
        #gets destination directory
        destination = self.destination_dir.get()
        #gets a list of files in the source directory
        source_files = os.listdir(source)
        #runs through each file in the source directory
        for i in source_files:
            #moves file from source to destination
            shutil.move(source + '/' + i, destination)
            print(i + ' was successfully transferred.')

    def exit_program(self):
        #root is the main GUI window
        #.destroy terminates root.mainloop() and all widgets in the GUI
        root.destroy()
        
        


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
