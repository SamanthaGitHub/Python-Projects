#
# Python:   3.9.7
#
# Author:   Samantha
#
# Purpose:  To determine which files in the list 'fileList' end with a '.txt',
#           add those files to the database, and print them to the console.


import sqlite3

fileList = ('information.docx','Hello.txt','myImage.png',\
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

conx = sqlite3.connect('AssnPython223.db') # connects to the database

with conx: # while connected, execute the following code
    cur = conx.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_filesAssn( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_files STRING \
        )")
    conx.commit()


for file in fileList: #loop thru the files to find those that end in '.txt'
    if file.endswith('.txt'):
        with conx:
            cur = conx.cursor()
            cur.execute("INSERT INTO tbl_filesAssn (col_files) VALUES (?)", (file,))
            # above will insert the files that end in '.txt' into the database AssnPython223 into tbl_filesAssn
            print(file)
conx.close() # closes the connection to the database

