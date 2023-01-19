#
#Version: Python 3.11.1
#
#Author: Jon Duea
#
#Purpose: To create a program that automatically detects newly created or modified files (within the last 24 hours)
#           from a user defined source and transfers them to a user defined destination.
#


import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os,time
import shutil
import datetime


class ParentWindow(Frame):
    #Function used to select the source directory
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #clears the content from the entry widget to allow the path to be inserted properly
        self.source_dir.delete(0, END)
        #inserts the user selection to the source_dir entry
        self.source_dir.insert(0, selectSourceDir)
        
    #Function used to select the destination directory
    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        #clears the content from the entry widget to allow the path to be inserted properly
        self.destination_dir.delete(0, END)
        #inserts the user selection to the destination_dir entry
        self.destination_dir.insert(0, selectDestDir)
        
    #Function to transfer the files from one directory to another
    def transferFiles(self):
        #Gets the current system time
        now = datetime.datetime.now()
        #Gets the source directory
        source = self.source_dir.get()
        #Gets the destination directory
        destination = self.destination_dir.get()
        #Gets a list of files from the source directory
        source_files = os.listdir(source)
        #Sets the cutoff time for what we consider new files
        ago = now-datetime.timedelta(hours=24)
        #Runs through each file in the source directory and retrieves there modified time
        for i in source_files:
            path = os.path.join(source, i)
            st = os.stat(path)
            mtime = datetime.datetime.fromtimestamp(st.st_mtime)
            #Here we compare the modified time of the file to our variable ago
            #to determine if it has been modified within the last 24 hours
            if mtime > ago:
                #moves each file that has been modified within the last 24 hours from the source to the destination
                shutil.move(source + '/' + i, destination)
                print(i + ' was successfully transferred.')
            
            
    
    #Function to exit the program
    def exit_program(self):
        #root is the GUI window and the tkinter method .destroy tells python to terminate the root.mainloop and close the window
        root.destroy()
        
    def __init__(self, master):
        Frame.__init__(self)
        #Title of GUI window
        self.master.title("File Transfer")
        #Creates the button to select files from source directory and positions it on the GUI
        self.sourceDir_btn = Button(text='Select Source', width=20, command=self.sourceDir)
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))
        #Creates the entry field for source directory selection and positions it in line with it's button on the GUI
        self.source_dir = Entry(width=75)
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))
        #Creates the button to select the destination of files from the destination directory and positions it on the GUI
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))
        #Creates the entry field for destination directory selection and positions it in line with it's button on the GUI
        self.destination_dir = Entry(width=75)
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15,10))
        #Creates the button to transfer the files from source to destination and positions it on the GUI
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))
        #Creates the button to exit the program and positions it on the GUI
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
