from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x',
               'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V',
               'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['#', '$', '%', '&','*', '+']

    password_list = []
    password_list += [random.choice(letters) for i in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for i in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for i in range(random.randint(2, 4))]
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get().title()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", 'r') as file:
                # Reading Old Data
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", 'w') as file:
                # Writing new data to file
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- Search ---------------------------------#
def search():
    website = website_input.get().title()

    # Reading data from json
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")

    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

# Canvas
canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 95, image=lock_image)
canvas.grid(column=1, row=0)

# Website Label
website_label = Label(text="Website")
website_label.config(padx=20, pady=20, font=("Arial", 10))
website_label.grid(column=0, row=1)

# Website Input
website_input = Entry(width=25)
website_input.grid(column=1, row=1)

# Search Button
search_btn = Button(text="Search", command=search)
search_btn.grid(column=2, row=1)

# Email Label
email_label = Label(text="Email/Username")
email_label.config(padx=20, pady=20, font=("Arial", 10))
email_label.grid(column=0, row=2)

# Email Input
email_input = Entry(width=35)
email_input.insert(0, "prasadnitin05@gmail.com")
email_input.grid(column=1, row=2, columnspan=2)

# Password Label
password_label = Label(text="Password")
password_label.config(padx=20, pady=20, font=("Arial", 10))
password_label.grid(column=0, row=3)

# Password Input
password_input = Entry(width=25)
password_input.grid(column=1, row=3)

# Generate Password Button
pass_button = Button(text="Generate", command=generate_password)
pass_button.grid(column=2, row=3)

# Add Button
add_button = Button(text="Add", width=28, command=save)
add_button.config(font=("Arial", 10, "bold"))
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
