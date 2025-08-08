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
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    web = entry_website.get()
    user_email = entry_user.get()
    password = entry_password.get()
    if len(web) == 0 or len(user_email) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="You can't take any label without any information.   ")
    else :
        answer = messagebox.askquestion(title="Save Data ", message= f"website : {web} \nusername or email : {user_email}\npassword : {password }")
        if answer :

            with open("data.txt", "a") as f:
                f.write(f"website : {web} | username or email : {user_email} | password : {password }\n")
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
entry_website = Entry( width= 50)
entry_website.grid( row = 1 , column = 1 , columnspan = 2  )
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

window.mainloop()
