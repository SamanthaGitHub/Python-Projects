# Python:   3.9.7
#
# Author:   Samantha
#
# Purpose:  To create a program to generate either a default or custom webpage.


import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master.title("Web Page Generator")
        #choosing custom or default label
        self.customLbl = Label(self.master, text="Enter custom text or click the Default HTML page button")
        self.customLbl.grid(row=0, column=0, padx=(10,10), pady=(10,10))
        #custom text entry
        self.customEntry = Entry(self.master, text="", width=120)
        self.customEntry.grid(row=1, column=0, columnspan=3, padx=(10,10), pady=(10,10))

        #button for default HTML page
        self.defaultBtn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.defaultBtn.grid(row=2, column=1, padx=(10,10), pady=(10,10))
        #button for custom text HTML page
        self.customBtn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        self.customBtn.grid(row=2, column=2, padx=(10,10), pady=(10,10))

    def defaultHTML(self):
        #creates HTML page with default h1 text in new browser tab
        htmlText = "Stay tunned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    def customHTML(self):
        #creates HTML page with custom h1 text in new browser tab
        htmlText = self.customEntry.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
