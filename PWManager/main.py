from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = pw_entry.get()

    with open("data.txt", "a") as data_file:
        data_file.write(f"{website} | {email} | {password}\n")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img) #tuple of x coor., y coor., and img
canvas.grid(row=0, column=1)

#labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
pw_label = Label(text="Password:")
pw_label.grid(row=3, column=0)

#entries
website_entry = Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus() #active cursor on website
email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "youremail@host.com") #prepopulates field with email
pw_entry = Entry(width=33)
pw_entry.grid(row=3, column=1)

#buttons
generate_pw_button = Button(text="Generate Password")
generate_pw_button.grid(row=3, column=2)
add_button = Button(text="Add", width=44, command=save_password())
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
