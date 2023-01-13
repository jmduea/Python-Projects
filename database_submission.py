#
#version: python 3.11.1
#
#Author: Jon Duea
#
#Purpose: To create a database, add the files that end in .txt from a list of files to the created database
#           and return the file names of the files added to the databse to the console.
#





import sqlite3

conn = sqlite3.connect('files.db')
#establishes a connection to the files db
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                col_filename TEXT)")    #creates a table with an id column and file name column
    conn.commit()
conn = sqlite3.connect('files.db')
#tuple of file names we will pick the .txt files from
fileList = ('infomation.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

# loops through each object in the tuple to find the files that end in .txt
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            # x will denote a one element tuple for each file ending in .txt
            cur.execute("INSERT INTO tbl_files (col_filename) values (?)", (x,))
            print(x)

conn.close()
