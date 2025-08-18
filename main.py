import json
import random
from tkinter import *
import string
from  tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password_fun():
    entry_password.delete(0, END)
    all_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    password_generated = "".join(random.choices(all_chars, k = 20))
    entry_password.insert(0, password_generated)
# ---------------------------- SEARCH ------------------------------- #
def find_password():
    website = entry_website.get()
    try:
        with open("data.json" , "r" ) as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showerror(title="Error" , message="No Data File Found. ")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Email : {email} \nPassword : {password}")
        else :
            messagebox.showinfo(title= "Error" , message = f"No details for {website} exists    "  )
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website  = entry_website.get()
    user_email = entry_user.get()
    password = entry_password.get()
    new_data = { website : {"email" : user_email , "password" : password }}
    if len(website) == 0 or len(user_email) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="You can't take any label without any information.   ")
    else :
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError :
            with open("data.json", "w") as data_file:
                json.dump(new_data , data_file , indent= 4)

        else :
            print(data)
            data.update(new_data)
            print(data)
            print(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data , data_file , indent = 4)
        finally:
            entry_password.delete(0, END)
            entry_website.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx= 50 , pady= 50  )
canvas = Canvas(window , height= 200 , width=200 )
photo = PhotoImage(file = "logo.png")
canvas.create_image(100 ,100, image = photo )
canvas.grid( row =  0  , column = 1 , pady = 20, padx = 20  )

# Website label and entry
website_label = Label(text = "website :")

website_label.grid(row = 1 , column = 0  )
entry_website = Entry( width= 30)
entry_website.grid( row = 1 , column = 1  )
entry_website.focus()
# Emai and Username
user_label = Label(text = "Email/Username :")
user_label.grid(row = 2 , column = 0)
entry_user = Entry(width= 50)
entry_user.grid( row = 2 , column = 1 , columnspan = 2  )

# Password
password_label = Label(text = "Password  :")
password_label.grid(row = 3 , column = 0 )
entry_password = Entry(width= 31  )
entry_password.grid( row = 3 , column = 1  )
generate_password = Button(text = "Generate Password" ,width= 15 , command =generate_password_fun   )
generate_password.grid(row = 3 , column = 2)

# Enter the data

button_add = Button( text= "Add" ,width= 47, highlightthickness= 0 , command = save_data  )
button_add.grid(row = 4 ,column =1 ,columnspan = 2 )

# Search for data

button_search = Button(text = "Search", width= 15, command = find_password)
button_search.grid(row = 1 , column = 2 )
window.mainloop()
