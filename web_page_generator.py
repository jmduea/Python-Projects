#
#Version: Python 3.11.1
#
#Author: Jon Duea
#
#Purpose: To create a tool to automatically create a basic html web page either from a predetermined "default" template
#           or by using text that a user can input into an entry box.
#
#



import tkinter as tk
from tkinter import *
import webbrowser


class ParentWindow(Frame):
    #Creates a function that will create an HTML Document
    def defaultHTML(self):
            htmlText = "Stay tuned for our amazing summer sale!"
            htmlFile = open("index.html", "w")
            htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
            htmlFile.write(htmlContent)
            htmlFile.close()
            webbrowser.open_new_tab("index.html")
            
    #Creates a function that will grab the users custom text entered into our entry box
    #and use that text to make an HTML document
    
    def customHTML(self):
        #This grabs the users input from the entry box
        customText = self.customtxt.get()
        #This creates the customindex.html file with write permissions
        customhtmlFile = open("customIndex.html", "w")
        customhtmlContent = "<html>\n<body>\n<h1>" + customText + "</h1>\n</body>\n</html>"
        #this writes the content of the customhtmlContent variable to the file
        customhtmlFile.write(customhtmlContent)
        customhtmlFile.close()
        #this opens the customIndex.html file in a new tab on your default webbrowser
        webbrowser.open_new_tab("customIndex.html")
        
        
    #laysout the widgets for the tkinter GUI Window
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        #Creates the text label that provides the user instructions on how to use the program
        #and positions it on the gui above the entry box
        self.lbl_programinfo = tk.Label(self.master, text="Enter custom text or click the Default HTML page button")
        self.lbl_programinfo.grid(row=0, column=0, padx=(10,0), pady=(10,0), sticky=N+W)
        #Creates the entry box for the user to input there custom text and positions it on the GUI
        self.customtxt = tk.Entry(self.master, text='')
        self.customtxt.grid(row=1, column=0, columnspan=3, padx=(10,10), pady=(10,10), sticky=N+E+W)
        #Creates the Default HTML Page button and positions it on the GUI
        self.defaultbtn = tk.Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.defaultbtn.grid(row=2, column=1, padx=(10,10), pady=(10,10))
        #Creates the custom button and positions it on the GUI
        self.custombtn = tk.Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        self.custombtn.grid(row=2, column=2, padx=(10,10), pady=(10,10))
    



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()