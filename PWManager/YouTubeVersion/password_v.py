import sqlite3, hashlib
from tkinter import *
from tkinter import simpledialog
from functools import partial
import uuid
import pyperclip
import base64
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet


#          ~*~* https://www.youtube.com/watch?v=EDxQKsyUg40 Password Manager Tutorial*~*~
backend = default_backend
salt = b'2444'

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend= backend
)

encryptionKey = 0

def encrypt(message: bytes, key: bytes) -> bytes:
    return Fernet(key).encrypt(message)

def decrypt(message: bytes, token: bytes) -> bytes:
    return Fernet(token).decrypt(message)


#Database code
with sqlite3.connect("pw_vault.db") as db:
    cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS masterpw(
id INTEGER PRIMARY KEY,
password TEXT NOT NULL,
recoveryKey TEXT NOT NULL);
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS vault(
id INTEGER PRIMARY KEY,
website TEXT NOT NULL,
username TEXT NOT NULL,
password TEXT NOT NULL);
''')

#Create Pop Up
def popUp(text):
    answer = simpledialog.askstring("input string", text)
    return answer

# Initiate window
window = Tk()

window.title("Password Vault")


def hash_password(inputs):
    hash = hashlib.sha256(inputs)
    hash = hash.hexdigest()

    return hash


def entry_screen():
    for widget in window.winfo_children():
        widget.destroy()

    window.geometry("250x150")
    # Master password creation
    mainlbl = Label(window, text="Create master password:")
    mainlbl.config(anchor=CENTER)
    mainlbl.pack()

    entrytxt = Entry(window, width=20, show="*")
    entrytxt.pack()
    entrytxt.focus()
    # Label for re-entering password
    reenterlbl = Label(window, text="Re-enter password:")
    reenterlbl.config(anchor=CENTER)
    reenterlbl.pack()

    reentertxt = Entry(window, width=20, show="*")
    reentertxt.pack()

    donotmatchlbl = Label(window)
    donotmatchlbl.pack()

    def save_password():
        if entrytxt.get() == reentertxt.get():
            sql = "DELETE FROM masterpw WHERE id=1" # clears field
            # password encryption
            cursor.execute(sql)
            hashedpw = hash_password(entrytxt.get().encode('utf-8'))
            key = str(uuid.uuid4().hex)
            recoveryKey = hash_password(key.encode('utf-8)'))

            global encryptionKey
            encryptionKey = base64.urlsafe_b64encode(kdf.derive(entrytxt.get().encode()))
            # saves hashed passwords
            insertpw = '''INSERT INTO masterpw(password, recoveryKey)
            VALUES(?,?)'''
            cursor.execute(insertpw, ((hashedpw), (recoveryKey)))
            db.commit()

            recovery_screen(key)
        else:
            donotmatchlbl.config(text="Passwords do not match")

    btn = Button(window, text="Save", command=save_password)
    btn.pack(pady=10)

def recovery_screen(key):
    for widget in window.winfo_children(): # clears screen
        widget.destroy()

    window.geometry("250x150")

    mainlbl = Label(window, text="Save this recovery key:")
    mainlbl.config(anchor=CENTER)
    mainlbl.pack()

    keylbl = Label(window, text=key)
    keylbl.config(anchor=CENTER)
    keylbl.pack()

    def copy_key():
        pyperclip.copy(keylbl.cget("text")) # pyperclip clipboard

    btn = Button(window, text="Copy Key", command=copy_key)
    btn.pack(pady=10)

    btn = Button(window, text="Done", command=password_vault)
    btn.pack(pady=10)

def reset_screen():
    for widget in window.winfo_children(): # clears screen
        widget.destroy()

    window.geometry("250x150")

    mainlbl = Label(window, text="Enter recovery key:")
    mainlbl.config(anchor=CENTER)
    mainlbl.pack()

    rectxt = Entry(window, width=20)
    rectxt.pack()
    rectxt.focus()

    keylbl = Label(window)
    keylbl.config(anchor=CENTER)
    keylbl.pack()

    def get_recovery_key():
        check_key = hash_password(str(rectxt.get()).encode('utf-8'))
        cursor.execute('SELECT * FROM masterpw WHERE id=1 AND recoveryKey = ?', [(check_key)])
        return cursor.fetchall()

    def check_recovery_key():
        checked = get_recovery_key()
        if checked:
            entry_screen()
        else: 
            rectxt.delete(0, 'end')
            keylbl.config(text="Wrong Key.")

    btn = Button(window, text="Check Key", command=check_recovery_key)
    btn.pack(pady=10)


def login_screen(): # first time screen
    for widget in window.winfo_children():
        widget.destroy()

    window.geometry("250x150")

    mainlbl = Label(window, text="Enter master password:")
    mainlbl.config(anchor=CENTER)
    mainlbl.pack()

    entrytxt = Entry(window, width=20, show="*")
    entrytxt.pack()
    entrytxt.focus()
    # Label for wrong password
    wrongpw = Label(window)
    wrongpw.config(anchor=CENTER)
    wrongpw.pack(side=TOP)

    def get_master_pw():
        checkhashedpw = hash_password(entrytxt.get().encode('utf-8'))
        global encryptionKey
        encryptionKey = base64.urlsafe_b64encode(kdf.derive(entrytxt.get().encode()))
        cursor.execute("SELECT * FROM masterpw WHERE id = 1 AND password = ?", [(checkhashedpw)])
        return cursor.fetchall()

    def check_password():
        match = get_master_pw()

        if match:
            password_vault()
        else:
            entrytxt.delete(0, 'end')
            wrongpw.config(text="Wrong password.")
    
    def reset_password():
        reset_screen()

    btn = Button(window, text="Submit", command=check_password)
    btn.pack(pady=7)

    btn1 = Button(window, text="Reset Password", command=reset_password)
    btn1.pack(pady=7)


def password_vault():
    for widget in window.winfo_children():
        widget.destroy()

    def addEntry():
        window.geometry()

        text1 = "Website"
        text2 = "Username"
        text3 = "Password"
        # pop ups
        website = encrypt(popUp(text1).encode(), encryptionKey)
        username = encrypt(popUp(text2).encode(), encryptionKey)
        password = encrypt(popUp(text3).encode(), encryptionKey)

        insert_fields = """INSERT INTO vault(website,username,password)
        VALUES(?,?,?)"""

        cursor.execute(insert_fields, (website, username, password))
        db.commit()

        password_vault()

    def removeEntry(input):
        cursor.execute("DELETE FROM vault WHERE id = ?", (input,))
        db.commit()

        password_vault()

    window.geometry("800x450")

    lbl = Label(window, text="Password Vault")
    lbl.grid(column=1)

    btn = Button(window, text="+", command=addEntry)
    btn.grid(column=1,pady=10)

    lbl = Label(window, text="Website")
    lbl.grid(row=2, column=0, padx=88)
    lbl = Label(window, text="Username")
    lbl.grid(row=2, column=1, padx=88)
    lbl = Label(window, text="Password")
    lbl.grid(row=2, column=2, padx=88)

    cursor.execute("SELECT * FROM vault")
    if(cursor.fetchall() != None):
        i = 0
        while True:
            cursor.execute("SELECT * FROM vault")
            array = cursor.fetchall()

            if (len(array) == 0):
                break
            # decryption
            lbl1 = Label(window, text=(decrypt(array[i][1], encryptionKey)), font=("Helvetica", 10))
            lbl1.grid(column=0, row=i+3)
            lbl2 = Label(window, text=(decrypt(array[i][2], encryptionKey)), font=("Helvetica", 10))
            lbl2.grid(column=1, row=i+3)
            lbl3 = Label(window, text=(decrypt(array[i][3], encryptionKey)), font=("Helvetica", 10))
            lbl3.grid(column=2, row=i+3)

            btn = Button(window, text="Delete", command=partial(removeEntry, array[i][0]))
            btn.grid(column=3, row=i+3, pady=10)

            i=i+1

            cursor.execute("SELECT * FROM vault")
            if (len(array) == 0):
                break


cursor.execute("SELECT * FROM masterpw")
if cursor.fetchall():
    login_screen()
else:
    entry_screen()


window.mainloop()
