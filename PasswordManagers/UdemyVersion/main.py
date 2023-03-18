import random
from tkinter import *
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # character creation
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    # password limitations
    nr_letters = random.randint(8, 10)
    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)
    # randomization of choices within respective categories
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    # randomizes the password character positions
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    pw_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    # retrieve values
    website = website_entry.get()
    email = email_entry.get()
    password = pw_entry.get()

    # json dictionary
    new_data = {website: {
        "email": email,
        "password": password
    }}

    # checks for empty fields, double checks user inputs, writes to the file, and clears the fields
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="You missed 1 or more fields.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
        # file doesn't exist
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        # file does exist
        else:
            # updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            pw_entry.delete(0, END)

    # data_file = open("data.txt", "a")
    # data_file.write(f"{website} | {email} | {password}\n")
    # data_file.close()


# ---------------------------- SEARCH PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No current details exist for {website}")



# ---------------------------- UI SETUP ------------------------------- #

# window setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(55, 70, image=logo_img) #tuple of x coor., y coor., and img
canvas.grid(row=0, column=1)

# labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
pw_label = Label(text="Password:")
pw_label.grid(row=3, column=0)

# entries
website_entry = Entry(width=33)
website_entry.grid(row=1, column=1)
website_entry.focus() #active cursor on website
email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "youremail@host.com") #prepopulates field with email
pw_entry = Entry(width=33)
pw_entry.grid(row=3, column=1)

# buttons
search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)
generate_pw_button = Button(text="Generate Password", command=generate_password)
generate_pw_button.grid(row=3, column=2)
add_button = Button(text="Add", width=44, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
